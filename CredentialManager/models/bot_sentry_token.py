class BotSentryToken(object):

    _swagger_types = {
        'id': 'int', 'app_name': 'str', 'dsn': 'str'
        }

    _attribute_map = {
        'id': 'id', 'app_name': 'app_name', 'dsn': 'dsn'
        }

    def __init__(self, id=None, app_name=None, dsn=None):
        '''BotSentryToken - a model defined in Swagger'''

        self._id = None
        self._app_name = None
        self._dsn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if app_name is not None:
            self.app_name = app_name
        self.dsn = dsn

    @property
    def id(self):
        '''Gets the id of this BotSentryToken.


        :return: The id of this BotSentryToken.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this BotSentryToken.


        :param id: The id of this BotSentryToken.
        :type: int
        '''

        self._id = id

    @property
    def app_name(self):
        '''Gets the app_name of this BotSentryToken.


        :return: The app_name of this BotSentryToken.
        :rtype: str
        '''
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        '''Sets the app_name of this BotSentryToken.


        :param app_name: The app_name of this BotSentryToken.
        :type: str
        '''

        self._app_name = app_name

    @property
    def dsn(self):
        '''Gets the dsn of this BotSentryToken.


        :return: The dsn of this BotSentryToken.
        :rtype: str
        '''
        return self._dsn

    @dsn.setter
    def dsn(self, dsn):
        '''Sets the dsn of this BotSentryToken.


        :param dsn: The dsn of this BotSentryToken.
        :type: str
        '''
        if dsn is None:
            raise ValueError("Invalid value for `dsn`, must not be `None`")

        self._dsn = dsn

    def to_dict(self):
        '''Returns the model properties as a dict'''
        result = {}

        for attr, _ in self._swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value
        if issubclass(BotSentryToken, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        '''Returns the string representation of the model'''
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        '''For `print` and `pprint`'''
        return self.to_str()

    def __eq__(self, other):
        '''Returns true if both objects are equal'''
        if not isinstance(other, BotSentryToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other