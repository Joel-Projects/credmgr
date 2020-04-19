from . import RedditApp
from .utils import resolveModelFromInput, resolveUser
from ..mixins import BaseModel, DeletableMixin, EditableMixin


class UserVerification(BaseModel, DeletableMixin, EditableMixin):
    _attrTypes = {
        **BaseModel._attrTypes,
        'id': 'int',
        'user_id': 'str',
        'redditor': 'str',
        'reddit_app_id': 'str',
        'extra_data': 'str',
        'owner_id': 'str'
        }

    _editableAttrs = ['user_id', 'redditor', 'reddit_app_id', 'extra_data']
    _path = '/user_verifications'
    _credmgrCallable = 'user_verification'
    _nameAttr = 'user_id'
    _canFetchByName = True
    _getByNamePath = 'get_redditor'

    def __init__(self, credmgr, id=None, user_id=None, redditor=None, reddit_app_id=None, extra_data=None, owner_id=None):
        super().__init__(credmgr, id)
        self.user_id = user_id
        self.reddit_app_id = reddit_app_id
        if redditor:
            self.redditor = redditor
        if extra_data:
            self.extra_data = extra_data
        self.owner_id = owner_id

    @staticmethod
    @resolveUser()
    def _create(_credmgr, user_id, reddit_app, redditor=None, extra_data=None, owner=None):
        '''Create a new User Verification

        **PERMISSIONS: At least Active user is required.**

        User Verifications for verifying a redditor with a User ID

        :param str user_id: User ID to associate Redditor with (required)
        :param Union[RedditApp,int,str] reddit_app: Reddit app the User Verification is for (required)
        :param str redditor: Redditor the User Verification is for. This is not usually set manually.
        :param dict extra_data: Extra JSON data to include with verification
        :param Union[User,int,str] owner: Owner of the verification. Requires Admin to create for other users.
        :return: UserVerification
        '''

        data = {'user_id': user_id, 'reddit_app_id': resolveModelFromInput(_credmgr, RedditApp, reddit_app)}
        if redditor:
            data['redditor'] = redditor
        if extra_data:
            data['extra_data'] = extra_data
        if owner:
            data['owner_id'] = owner
        return _credmgr.post('/user_verifications', data=data)