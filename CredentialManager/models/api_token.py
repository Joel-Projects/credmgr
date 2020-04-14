from ..mixins import BaseModel, DeletableMixin, EditableMixin, ToggableMixin


class ApiToken(BaseModel, DeletableMixin, EditableMixin, ToggableMixin):
    _attr_types = {
        **BaseModel._attr_types,
        'name': 'str',
        'token': 'str',
        'owner_id': 'int',
        'enabled': 'bool',
        'created': 'datetime',
        'updated': 'datetime',
        'last_used': 'datetime'
        }

    _attribute_map = {
        **BaseModel._attribute_map,
        'name': 'name',
        'token': 'token',
        'owner_id': 'owner_id',
        'enabled': 'enabled',
        'created': 'created',
        'updated': 'updated',
        'last_used': 'last_used'
        }
    _path = '/api_tokens'
    _nameAttr = 'name'
    editableAttrs = ['name', 'enabled']

    def __init__(self, credmgr, id=None, name=None, token=None, owner_id=None, enabled=None, created=None, updated=None, last_used=None):
        super(ApiToken, self).__init__(credmgr, id)
        if name:
            self.name = name
        if token:
            self.token = token
        if owner_id:
            self.owner_id = owner_id
        if enabled:
            self.enabled = enabled
        if created:
            self.created = created
        if updated:
            self.updated = updated
        if last_used:
            self.last_used = last_used
