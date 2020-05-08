import json

from ..exceptions import InitializationError
from ..mixins import BaseModel, DeletableMixin, EditableMixin, ToggableMixin


class User(BaseModel, DeletableMixin, EditableMixin, ToggableMixin):
    _attrTypes = {
        **BaseModel._attrTypes,
        'id': 'int',
        'username': 'str',
        'is_active': 'bool',
        'is_regular_user': 'bool',
        'is_admin': 'bool',
        'default_settings': 'dict(str, str)',
        'reddit_username': 'str',
        'created': 'datetime',
        'updated': 'datetime',
        'reddit_apps': 'list[RedditApp]',
        'sentry_tokens': 'list[SentryToken]',
        'database_credentials': 'list[DatabaseCredential]'
    }
    _editableAttrs = ['username', 'isActive', 'isRegularUser', 'isAdmin', 'defaultSettings', 'redditUsername']
    _path = '/users'
    _credmgrCallable = 'user'
    _nameAttr = 'username'
    _enabledAttr = 'isActive'
    _canFetchByName = True
    _fetchNameAttr = _nameAttr

    def __init__(self, credmgr, id=None, username=None, isActive=None, isRegularUser=None, isAdmin=None, defaultSettings=None, redditUsername=None, created=None, updated=None, redditApps=None, sentryTokens=None, databaseCredentials=None):
        super(User, self).__init__(credmgr, id)
        self._apps = {}
        if username:
            self.username = username
        if isActive is not None:
            self._fetched = True
            self.isActive = isActive
        if isRegularUser is not None:
            self.isRegularUser = isRegularUser
        if isAdmin is not None:
            self.isAdmin = isAdmin
        if defaultSettings is not None:
            self.defaultSettings = defaultSettings
        if redditUsername is not None:
            self.redditUsername = redditUsername
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if redditApps:
            self._apps['redditApps'] = redditApps
        if sentryTokens:
            self._apps['sentryTokens'] = sentryTokens
        if databaseCredentials:
            self._apps['databaseCredentials'] = databaseCredentials

    @staticmethod
    def _create(_credmgr, username, password, defaultSettings=None, redditUsername=None, isAdmin=False, isActive=True, isRegularUser=True, isInternal=False):
        '''Create a new User

        **PERMISSIONS: Admin role is required.**

        :param str username: Username for new user (Example: ```spaz```) (required)
        :param str password: Password for new user (Example: ```supersecurepassword```) (required)
        :param dict defaultSettings: Default values to use for new apps (Example: ```{"databaseFlavor": "postgres", "databaseHost": "localhost"}```)
        :param str redditUsername: User's Reddit username (Example: ```LilSpazJoekp```)
        :param bool isAdmin: Is the user an admin? Allows the user to see all objects and create users (Default: ``false``)
        :param bool isActive: Is the user active? Allows the user to sign in (Default: ``true``)
        :param bool isRegularUser: (Internal use only)
        :param bool isInternal: (Internal use only)
        :return: User

        '''
        additionalParams = {}
        if defaultSettings:
            additionalParams['default_settings'] = json.dumps(defaultSettings)
        if isAdmin:
            additionalParams['is_admin'] = isAdmin
        if isActive:
            additionalParams['is_active'] = isActive
        if isRegularUser:
            additionalParams['is_regular_user'] = isRegularUser
        if isInternal:
            additionalParams['is_internal'] = isInternal
        if redditUsername:
            additionalParams['reddit_username'] = redditUsername
        return _credmgr.post('/users', data={'username': username, 'password': password, **additionalParams})

    def apps(self, only=None):
        '''

        :param str only: Pass one of ``redditApps``, ``sentryTokens``, ``databaseCredentials`` to only get those types
        :return: Union[dict,list[Union[RedditApp,SentryToken,DatabaseCredential]]]
        '''
        if not self._apps:
            response = self._credmgr.get(f'/users/{self.id}/apps')
            self._apps = response._apps
        if only:
            if only in ['redditApps', 'sentryTokens', 'databaseCredentials']:
                return self._apps[only]
            else:
                raise InitializationError(f"App type: {only} is not valid. Only 'reddit_apps', 'sentry_tokens', and 'database_credentials' are valid.")
        return self._apps