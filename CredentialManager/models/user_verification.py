from ..mixins import BaseModel, DeletableMixin, EditableMixin


class UserVerification(BaseModel, DeletableMixin, EditableMixin):

    _attr_types = {
        **BaseModel._attr_types,
        'id': 'int',
        'user_id': 'str',
        'redditor': 'str',
        'reddit_app_id': 'str',
        'extra_data': 'str',
        'owner_id': 'str'
        }

    _attribute_map = {
        **BaseModel._attribute_map,
        'id': 'id',
        'user_id': 'user_id',
        'redditor': 'redditor',
        'reddit_app_id': 'reddit_app_id',
        'extra_data': 'extra_data',
        'owner_id': 'owner_id'
        }
    editableAttrs = ['user_id', 'redditor', 'reddit_app_id', 'extra_data']
    _path = '/user_verifications'
    def __init__(self, credmgr, id=None, user_id=None, redditor=None, reddit_app_id=None, extra_data=None, owner_id=None):
        super().__init__(credmgr, id)
        if user_id:
            self.user_id = user_id
        if redditor:
            self.redditor = redditor
        if reddit_app_id:
            self.reddit_app_id = reddit_app_id
        if extra_data:
            self.extra_data = extra_data
        if owner_id:
            self.owner_id = owner_id