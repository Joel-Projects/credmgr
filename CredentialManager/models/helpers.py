from . import Bot, RedditApp, User, UserVerification
from ..exceptions import InitializationError
from ..mixins import BaseModel


class Paginator:

    def __init__(self, credmgr, model, batchSize=20, limit=None, owner=None):
        '''Initialize a ListGenerator instance.

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param model: A CredentialManager model to list.
        :param int batchSize: The number of items to fetch at a time. If ``batchSize`` is None, it will fetch them 100 at a time. (default: 20).
        :param int limit: The maximum number of items to get.
        :param Union[int, User, str] owner: Owner to filter the items by.
        '''
        self._credmgr = credmgr
        self._model = model(self._credmgr)
        self.batchSize = batchSize
        self.limit = limit
        self.owner = None
        if isinstance(owner, User):
            self.owner = owner.id
        elif isinstance(owner, int):
            self.owner = owner
        elif isinstance(owner, str):
            self.owner = self._credmgr.user(owner).id
        self._itemsReturned = 0
        self._completed = False
        self._offset = 0
        self._currentItemIndex = None
        self._response = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit is not None and self._itemsReturned >= self.limit:
            raise StopIteration()

        if self._response is None or self._currentItemIndex >= len(self._response):
            self._next()

        self._currentItemIndex += 1
        self._itemsReturned += 1
        return self._response[self._currentItemIndex - 1]

    def _next(self):
        if self._completed:
            raise StopIteration()
        params = dict(limit=self.batchSize, offset=self._offset)
        if self.owner:
            params['owner_id'] = self.owner
        self._response = self._credmgr.get(self._model._path, params=params)
        self._currentItemIndex = 0
        if not self._response:
            raise StopIteration()
        if self._response and len(self._response) == self.batchSize:
            self._offset += self.batchSize
        else:
            self._completed = True

class BaseHelper(BaseModel):
    _model = None

    def __call__(self, id=None, name=None, batchSize=20, limit=None, owner=None):
        kwargs = {}
        byName = False
        if isinstance(id, str):
            byName = True
            name = id
            id = None
        if id:
            kwargs['id'] = id
        if name:
            if self._model._canFetchByName:
                kwargs[self._model._nameAttr] = name
            else:
                raise InitializationError(f'Cannot get {self._model.__name__!r} by name')
        if not (id or name):
            return self._model(self._credmgr).listItems(batchSize=batchSize, limit=limit, owner=owner)
        item = self._model(self._credmgr, **kwargs)
        item.fetch(byName)
        return item

class UserHelper(BaseHelper):
    _model = User

    def __call__(self, id=None, name=None, batchSize=20, limit=None):
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
            return User(self._credmgr).listItems(batchSize=batchSize, limit=limit)
        item = User(self._credmgr, **kwargs)
        item.fetch(byName)
        return item

    def create(self, username, password, default_settings=None, is_admin=False, is_active=True, is_regular_user=True, is_internal=False, reddit_username=None) -> User:
        '''Create a new user

        **PERMISSIONS: Admin role is required.**

        :param str username: Username for new user (Example: ```spaz```) (required)
        :param str password: Password for new user (Example: ```supersecurepassword```) (required)
        :param str default_settings: Default values to use for new apps (Example: ```{"database_flavor": "postgres", "database_host": "localhost"}```)
        :param bool is_admin: Is the user an admin? Allows the user to see all objects and create users (Default: ``False``)
        :param bool is_active: Is the user active? Allows the user to sign in (Default: ``True``)
        :param bool is_regular_user: (Internal use only)
        :param bool is_internal: (Internal use only)
        :param str reddit_username:
        :return: User
        '''

        return self._model._create(self._credmgr, username, password, default_settings, is_admin, is_active, is_regular_user, is_internal, reddit_username)

class BotHelper(BaseHelper):
    _model = Bot

    def create(self, app_name, reddit_app=None, sentry_token=None, database_credential=None, owner=None) -> Bot:
        '''Create a new Bot

        **PERMISSIONS: At least Active user is required.**

        Bots are used for grouping apps into a single request

        :param str app_name: Name of the Bot (required)
        :param Union[RedditApp,int] reddit_app: Reddit App the bot will use
        :param Union[SentryToken,int] sentry_token: Sentry Token the bot will use
        :param Union[DatabaseCredential,int] database_credential: Database Credentials the bot will use
        :param Union[User,int,str] owner: Owner of the bot. Requires Admin to create for other users.
        :return: Bot
        '''

        return self._model._create(self._credmgr, app_name, reddit_app, sentry_token, database_credential, owner)

class RedditAppHelper(BaseHelper):
    _model = RedditApp

    def create(self, app_name, client_id, user_agent=None, app_type='web', redirect_uri='https://credmgr.jesassn.org/oauth2/reddit_callback', client_secret=None, short_name=None, app_description=None, enabled=True, owner=None) -> RedditApp:
        '''Create a new RedditApp

        **PERMISSIONS: At least Active user is required.**

        Reddit Apps are used for interacting with reddit

        :param str app_name: (required)
        :param str client_id: Client ID of the Reddit App (required)
        :param str user_agent: User agent used for requests to Reddit's API (required, defaults to user set default, then to 'python:{app_name} by /u/{redditUsername}' if currentUser.reddit_username is set or 'python:{app_name}' if it is not set)
        :param str app_type: Type of the app. One of `web`, `installed`, or `script` (default: 'web')
        :param str redirect_uri: Redirect URI for Oauth2 flow. Defaults to user set redirect uri (default: 'https://credmgr.jesassn.org/oauth2/reddit_callback')
        :param str client_secret: Client secret of the Reddit App
        :param str short_name: Short name of the Reddit App
        :param str app_description: Description of the Reddit App
        :param bool enabled: Allows the app to be used
        :param int owner: Owner of the app. Requires Admin to create for other users.
        :return: RedditApp
        '''
        if not user_agent:
            redditUsername = self._credmgr.currentUser.reddit_username
            redditUsernameStr = ''
            if redditUsername:
                redditUsernameStr = f' by /u/{redditUsername}'
            user_agent = self._credmgr.getUserDefault('user_agent', f'python:{app_name}{redditUsernameStr}')
        return self._model._create(self._credmgr, app_name, client_id, user_agent, app_type, redirect_uri, client_secret, short_name, app_description, enabled, owner)

class UserVerificationHelper(BaseHelper):
    _model = UserVerification

    def create(self, user_id, reddit_app_id, redditor=None, extra_data=None, owner=None) -> RedditApp:
        '''Create a new User Verification

        **PERMISSIONS: At least Active user is required.**

        User Verifications for verifying a redditor with a User ID

        :param str user_id: User ID to associate Redditor with (required)
        :param int reddit_app_id: Reddit app the User Verification is for (required)
        :param str redditor: Redditor the User Verification is for
        :param str extra_data: Extra JSON data to include with verification
        :param int owner: Owner of the verification. Requires Admin to create for other users.
        :return: UserVerification
        '''
        return self._model._create(self._credmgr, user_id=user_id, reddit_app=reddit_app_id, redditor=redditor, extra_data=extra_data, owner=owner)

    def __call__(self, user_id=None, reddit_app_id=None, batchSize=20, limit=None, owner=None):
        kwargs = {}
        if user_id:
            kwargs['user_id'] = user_id
        if reddit_app_id:
            kwargs['reddit_app_id'] = reddit_app_id
        if not user_id:
            return self._model(self._credmgr).listItems(batchSize=batchSize, limit=limit, owner=owner)
        item = self._model(self._credmgr, **kwargs)
        item.fetch(True)
        return item