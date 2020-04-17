from ..mixins import BaseApp


class Bot(BaseApp):
    _attr_types = {
        **BaseApp._attr_types, 'reddit_app': 'RedditApp', 'sentry_token': 'SentryToken', 'database_credential': 'DatabaseCredential'
        }

    _attribute_map = {
        **BaseApp._attribute_map, 'reddit_app': 'reddit_app', 'sentry_token': 'sentry_token', 'database_credential': 'database_credential'
        }
    _editableAttrs = BaseApp._editableAttrs + ['reddit_id', 'sentry_id', 'database_id']
    _path = '/bots'
    _canFetchByName = True
    def __init__(self, credmgr, id=None, app_name=None, enabled=None, owner_id=None, reddit_app=None, sentry_token=None, database_credential=None):
        super(Bot, self).__init__(credmgr, id, app_name, enabled, owner_id)
        self.reddit_app = reddit_app
        self.sentry_token = sentry_token
        self.database_credential = database_credential

    @staticmethod
    def _create(_credmgr, name, reddit_app, sentry_token, database_credential, owner=None):
        '''Create a new Bot

        **PERMISSIONS: At least Active user is required.**   Bots are used for grouping apps into a single request

        :param str name: Name of the Bot (required)
        :param Union[RedditApp,int] reddit_app: Reddit App the bot will use
        :param Union[SentryToken,int] sentry_token: Sentry Token the bot will use
        :param Union[DatabaseCredential,int] database_credential: Database Credentials the bot will use
        :param Union[User,int,str] owner: Owner of the bot. Requires Admin to create for other users.
        :return: Bot
        '''

        from . import DatabaseCredential, RedditApp, SentryToken, User
        additionalParams = {}
        if isinstance(reddit_app, RedditApp):
            reddit_app = reddit_app.id
        if reddit_app:
            additionalParams['reddit_id'] = reddit_app
        if isinstance(sentry_token, SentryToken):
            sentry_token = sentry_token.id
        if sentry_token:
            additionalParams['sentry_id'] = sentry_token
        if isinstance(database_credential, DatabaseCredential):
            database_credential = database_credential.id
        if database_credential:
            additionalParams['database_id'] = database_credential
        if isinstance(owner, User):
            owner = owner.id
        elif isinstance(owner, str):
            owner = User(_credmgr, username=owner).id
        if owner:
            additionalParams['owner_id'] = owner
        return _credmgr.post('/bots', data={'app_name': name, **additionalParams})

    def edit(self, **kwargs):
        for key, value in kwargs.items():
            if key in ['reddit_app', 'sentry_token', 'database_credential']:
                newKey = f'{key.split("_")[0]}_id'
                kwargs[newKey] = kwargs.pop(key)
        super(Bot, self).edit(**kwargs)