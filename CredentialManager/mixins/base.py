class BaseModel(object):
    _attr_types = {'id': 'int'}
    _attribute_map = {'id': 'id'}
    _path = None
    _nameAttr = None
    _canFetchByName = False

    def __init__(self, credmgr, id=None, name=None):
        self._credmgr = credmgr
        self.id = id
        self.fetched = False
        if self._nameAttr and self._canFetchByName:
            setattr(self, self._nameAttr, name)

    def __getattr__(self, attribute):
        '''Return the value of `attribute`.'''
        if not attribute.startswith("_"):
            if not self.fetched:
                self.fetch()
            return self.__dict__.get(attribute, None)
        else:
            return None

    def get(self, id):
        self.__dict__ = self._credmgr.get(f'{self._path}/{id}').__dict__
        self.fetched = True

    def getByName(self, name):
        self.__dict__ = self._credmgr.post(f'{self._path}/by_name', data={self._nameAttr: name}).__dict__
        self.fetched = True

    def fetch(self, byName=False):
        if byName and self._canFetchByName:
            self.getByName(getattr(self, self._nameAttr))
        else:
            self.get(self.id)

    def list(self, limit=10, offset=0, owner_id=None):
        params = dict(limit=limit, offset=offset)
        if owner_id:
            params['owner_id'] = owner_id
        return self._credmgr.get(self._path, params=params)

    def to_dict(self):
        result = {}

        for attr, _ in self._attr_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value
        if issubclass(type(self), dict):
            for key, value in self.items():
                result[key] = value
        return result

    def __repr__(self):
        ## ownerRepr = ''
        ## if hasattr(self, 'owner'):
        ##     ownerRepr = f', owner={self.owner.username!r}'
        ## return f'<{self.__class__.__name__} id={self.id}, {self._nameAttr}={getattr(self, self._nameAttr)!r}{ownerRepr}>'
        return f'<{self.__class__.__name__} id={self.id}, {self._nameAttr}={getattr(self, self._nameAttr)!r}>'

    def __eq__(self, other):
        '''Returns true if both objects are equal'''
        if not isinstance(other, type(self)):
            return False

        return self.__dict__ == other.__dict__