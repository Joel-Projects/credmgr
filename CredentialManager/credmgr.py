from . import models
from .api_client import ApiClient
from .config import Config


ApiToken = models.ApiToken
User = models.User
Bot = models.Bot
RedditApp = models.RedditApp
RefreshToken = models.RefreshToken
UserVerification = models.UserVerification
SentryToken = models.SentryToken
DatabaseCredential = models.DatabaseCredential

class CredentialManager(object):
    _default = None

    def __init__(self, host="https://credmgr.jesassn.org/api/v1", **kwargs):
        self.config = Config(host=host, **kwargs)
        self._client = ApiClient(self, self.config)

        self.api_token = models.ApiTokenHelper(self)
        self.user = models.UserHelper(self)
        self.bot = models.BotHelper(self)
        # self.reddit_app = models.RedditAppHelper(self)
        # self.refresh_token = models.RefreshTokenHelper(self)
        # self.user_verification = models.UserVerificationHelper(self)
        # self.sentry_token = models.SentryTokenHelper(self)
        # self.database_credential = models.DatabaseCredentialHelper(self)

    def api_tokens(self, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if owner_id:
            kwargs['owner_id'] = id
        return ApiToken(self, **kwargs).list(limit=limit, offset=offset)

    def users(self, limit=10, offset=0):
        kwargs = {}
        return User(self, **kwargs).list(limit=limit, offset=offset)

    def bots(self, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if owner_id:
            kwargs['owner_id'] = id
        return Bot(self, **kwargs).list(limit=limit, offset=offset)

    def reddit_apps(self, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if owner_id:
            kwargs['owner_id'] = id
        return RedditApp(self, **kwargs).list(limit=limit, offset=offset)

    def refresh_tokens(self, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if owner_id:
            kwargs['owner_id'] = id
        return RefreshToken(self, **kwargs).list(limit=limit, offset=offset)

    def user_verifications(self, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if owner_id:
            kwargs['owner_id'] = id
        return UserVerification(self, **kwargs).list(limit=limit, offset=offset)

    def sentry_tokens(self, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if owner_id:
            kwargs['owner_id'] = id
        return SentryToken(self, **kwargs).list(limit=limit, offset=offset)

    def database_credentials(self, owner_id=None, limit=10, offset=0):
        kwargs = {}
        if owner_id:
            kwargs['owner_id'] = id
        return DatabaseCredential(self, **kwargs).list(limit=limit, offset=offset)

    def currentUser(self):
        return self.get(User, '/users/me')

    def get(self, model, path, **kwargs):
        if not path:
            path = model._path
        item, code, headers = self._client.call_api(path, 'GET', response_type=model, **kwargs)
        return item

    def post(self, model, path, **kwargs):
        if not path:
            path = model._path
        item, code, headers = self._client.call_api(path, 'POST', response_type=model, **kwargs)
        return item

    def patch(self, model, path, **kwargs):
        if not path:
            path = model._path
        item, code, headers = self._client.call_api(path, 'PATCH', response_type=model)
        return item

    def delete(self, model, path, **kwargs):
        if not path:
            path = model._path
        item, code, headers = self._client.call_api(path, 'DELETE')
        return item