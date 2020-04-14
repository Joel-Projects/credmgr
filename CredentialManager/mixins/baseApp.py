from ..mixins import BaseModel, DeletableMixin, EditableMixin, ToggableMixin, OwnerMixin


class BaseApp(BaseModel, DeletableMixin, EditableMixin, ToggableMixin, OwnerMixin):
    _attr_types = {**BaseModel._attr_types, 'app_name': 'str', 'enabled': 'bool', 'owner_id': 'int'}
    _attribute_map = {**BaseModel._attribute_map, 'app_name': 'app_name', 'enabled': 'enabled', 'owner_id': 'owner_id'}
    _nameAttr = 'app_name'
    _editableAttrs = ['app_name', 'enabled']
    def __init__(self, credmgr, id=None, app_name=None, enabled=None, owner_id=None):
        super(BaseApp, self).__init__(credmgr, id)
        if app_name:
            self.app_name = app_name
        if enabled:
            self.enabled = enabled
        if owner_id:
            self.owner_id = owner_id