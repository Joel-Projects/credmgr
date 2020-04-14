from ..mixins import BaseModel, DeletableMixin, EditableMixin, ToggableMixin


class User(BaseModel, DeletableMixin, EditableMixin, ToggableMixin):

    _attr_types = {**BaseModel._attr_types,
        'id': 'int',
        'username': 'str',
        'is_active': 'str',
        'is_regular_user': 'str',
        'is_admin': 'str',
        'default_settings': 'dict(str, str)',
        'created': 'datetime',
        'updated': 'datetime'
        }

    _attribute_map = {**BaseModel._attribute_map,
        'id': 'id',
        'username': 'username',
        'is_active': 'is_active',
        'is_regular_user': 'is_regular_user',
        'is_admin': 'is_admin',
        'default_settings': 'default_settings',
        'created': 'created',
        'updated': 'updated'
        }
    _path = '/users'
    _nameAttr = 'username'
    _enabledAttr = 'is_active'
    _canFetchByName = True
    def __init__(self, credmgr, id=None, username=None, is_active=None, is_regular_user=None, is_admin=None, default_settings=None, created=None, updated=None):
        super().__init__(credmgr, id)
        if username:
            self.username = username
        if is_active is not None:
            self.is_active = is_active
        if is_regular_user is not None:
            self.is_regular_user = is_regular_user
        if is_admin is not None:
            self.is_admin = is_admin
        if default_settings is not None:
            self.default_settings = default_settings
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @staticmethod
    def _create(_credmgr, username, password, default_settings=None, is_admin=False, is_active=True, is_regular_user=True, is_internal=False, reddit_username=None):
        '''Create a new User

        **PERMISSIONS: Admin role is required.**

        :param str username: Username for new user (Example: ```spaz```) (required)
        :param str password: Password for new user (Example: ```supersecurepassword```) (required)
        :param str default_settings: Default values to use for new apps (Example: ```{"database_flavor": "postgres", "database_host": "localhost"}```)
        :param bool is_admin: Is the user an admin? Allows the user to see all objects and create users (Default: ``false``)
        :param bool is_active: Is the user active? Allows the user to sign in (Default: ``true``)
        :param bool is_regular_user: (Internal use only)
        :param bool is_internal: (Internal use only)
        :param str reddit_username:
        :return: User

        '''
        additionalParams = {}
        if default_settings:
            additionalParams['default_settings'] = default_settings
        if is_admin:
            additionalParams['is_admin'] = is_admin
        if is_active:
            additionalParams['is_active'] = is_active
        if is_regular_user:
            additionalParams['is_regular_user'] = is_regular_user
        if is_internal:
            additionalParams['is_internal'] = is_internal
        if reddit_username:
            additionalParams['reddit_username'] = reddit_username
        return _credmgr.post('/bots', data={'username': username, 'password': password, **additionalParams})
