from ..mixins import BaseModel
from ..models import ApiToken, User, Bot, RedditApp, RefreshToken, UserVerification, SentryToken, DatabaseCredential

class ApiTokenHelper(BaseModel):

    def __call__(self, id=None, name=None, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if id:
            kwargs['id'] = id
        if name:
            kwargs['name'] = name
        if owner_id:
            kwargs['owner_id'] = owner_id
        if not (id or name):
            return ApiToken(self, **kwargs).list(limit=limit, offset=offset)
        item = ApiToken(self, **kwargs)
        item.fetch()
        return item

class UserHelper(BaseModel):

    def __call__(self, id=None, name=None, owner_id=None, limit=10, offset=0):
        kwargs = {}
        byName = False
        if isinstance(id, str):
            byName = True
            name = id
            id = None
        if id:
            kwargs['id'] = id
        if name:
            kwargs['username'] = name
        if not (id or name):
            return User(self._credmgr, **kwargs).list(limit=limit, offset=offset)
        item = User(self._credmgr, **kwargs)
        item.fetch(byName)
        return item

    def create(self, username, password, default_settings=None, is_admin=False, is_active=True, is_regular_user=True, is_internal=False, reddit_username=None) -> User:
        '''Create a new user

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

        return User._create(self._credmgr, username, password, default_settings, is_admin, is_active, is_regular_user, is_internal, reddit_username)

class BotHelper(BaseModel):

    def __call__(self, id=None, name=None, owner_id=None, limit=10, offset=0):
        kwargs = {}
        byName = False
        if isinstance(id, str):
            byName = True
            name = id
            id = None
        if id:
            kwargs['id'] = id
        if name:
            kwargs['app_name'] = name
        if owner_id:
            kwargs['owner_id'] = owner_id
        if not (id or name):
            return Bot(self._credmgr, **kwargs).list(limit=limit, offset=offset)
        item = Bot(self._credmgr, **kwargs)
        item.fetch(byName)
        return item

    def create(self, name, reddit_app=None, sentry_token=None, database_credential=None, owner=None) -> Bot:
        '''Create a new Bot

        **PERMISSIONS: At least Active user is required.**   Bots are used for grouping apps into a single request

        :param str name: Name of the Bot (required)
        :param Union[RedditApp,int] reddit_app: Reddit App the bot will use
        :param Union[SentryToken,int] sentry_token: Sentry Token the bot will use
        :param Union[DatabaseCredential,int] database_credential: Database Credentials the bot will use
        :param Union[User,int,str] owner: Owner of the bot. Requires Admin to create for other users.
        :return: Bot
        '''

        return Bot._create(self._credmgr, name, reddit_app, sentry_token, database_credential, owner)