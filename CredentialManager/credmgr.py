from urllib.parse import urljoin

from requests import Session

from . import models
from .auth import ApiTokenAuth
from .exceptions import InitializationError
from .requestor import Requestor
from .serializer import Serializer


ApiToken = models.ApiToken
User = models.User
Bot = models.Bot
RedditApp = models.RedditApp
RefreshToken = models.RefreshToken
UserVerification = models.UserVerification
SentryToken = models.SentryToken
DatabaseCredential = models.DatabaseCredential

def setOwner(owner_id, data):
    if owner_id:
        data['owner_id'] = owner_id

class CredentialManager(object):
    '''The CredentialManager class provides convenient access to CredentialManager's API.

    Instances of this class are the gateway to interacting with CredentialManager's API
    through PRAW. The canonical way to obtain an instance of this class is via:


    .. code-block:: python

        import CredentialManager
        credmgr = CredentialManager.client(api_token='L_iqbGj_Aeep3Ws5DH3LOEQPmw8UZ6ek')


    '''
    _default = None
    _endpoint = '/api/v1'

    def __init__(self, host='https://credmgr.jesassn.org', api_token=None, username=None, password=None, session_class=None, session_kwargs={}):
        '''Initialize a CredentialManager instance.

        :param str host: Hostname to use for interacting with the API (default: ``https://credmgr.jesassn.org``)
        :param str api_token: API Token used for authentication (Note: cannot be used when ``username`` and ``password`` params are passed)
        :param str username: Username to use for interacting with the API (Note: Cannot be used when ``api_token`` param is passed)
        :param str password: Password to use for interacting with the API (Note: Cannot be used when ``api_token`` param is passed)
        :param Session session_class: A Session class that will be used to create a requestor. If not set, use ``requests.Session`` (default: None).
        :param dict session_kwargs: Dictionary with additional keyword arguments used to initialize the session (default: None).

        .. warning::
             Using an API Token instead of a username/password is strongly recommended!

        The ``session_class`` and ``session_kwargs`` allow for
        customization of the session :class:`.CredentialManager` will use. This allows,
        e.g., easily adding behavior to the requestor or wrapping its
        |Session|_ in a caching layer. Example usage:

        .. |Session| replace:: ``Session``
        .. _Session: https://2.python-requests.org/en/master/api/#requests.Session

        .. code-block:: python

           import json, betamax, requests

           class JSONDebugRequestor(Requestor):
               def request(self, *args, **kwargs):
                   response = super().request(*args, **kwargs)
                   print(json.dumps(response.json(), indent=4))
                   return response

           my_session = betamax.Betamax(requests.Session())
           reddit = CredentialManager.client(..., session_class=JSONDebugRequestor, session_kwargs={'session': my_session})
        '''
        self._host = urljoin(host, self._endpoint)
        if all([api_token, username, password]):
            raise InitializationError('Either api_token or username/password pair can be passed, both cannot be passed')
        if api_token:
            self._auth = ApiTokenAuth(api_token)
        elif username and password:
            self._auth = (username, password)
        else:
            raise InitializationError('api_token or an username/password pair must be passed')

        self._requestor = Requestor(self._host, self._auth, session_class, **session_kwargs)
        self.serializer = Serializer(self)
        self.current_user = self.currentUser()

        self.api_token = models.ApiTokenHelper(self)
        '''An instance of :class:`.ApiTokenHelper`.

        Provides the interface for interacting with :class:`.ApiToken`.
        For example to get a ``api_token`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            api_token = credmgr.api_token(1)
            print(api_token.id)
        
        .. note::
            API Tokens cannot be created via the API.
        '''
        self.user = models.UserHelper(self)
        '''An instance of :class:`.UserHelper`.

        Provides the interface for interacting with :class:`.User`.
        For example to get a ``user`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            user = credmgr.user(1)
            print(user.id)
        
        To create a ``user`` do:
        
        ..code-block:: python
            user = credmgr.user.create(**userKwargs)
        
        See :meth:`~.UserHelper.create` for the required params.
        '''
        self.bot = models.BotHelper(self)
        '''An instance of :class:`.BotHelper`.

        Provides the interface for interacting with :class:`.Bot`.
        For example to get a ``bot`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            bot = credmgr.bot(1)
            print(bot.id)
        
        To create a ``bot`` do:
        
        ..code-block:: python
            bot = credmgr.bot.create(**botKwargs)
        
        See :meth:`~.BotHelper.create` for the required params.
        '''

        ## self.reddit_app = models.RedditAppHelper(self)
        '''An instance of :class:`.RedditAppHelper`.

        Provides the interface for interacting with :class:`.RedditApp`.
        For example to get a ``reddit_app`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            reddit_app = credmgr.reddit_app(1)
            print(reddit_app.id)
        
        To create a ``reddit_app`` do:
        
        ..code-block:: python
            reddit_app = credmgr.reddit_app.create(**reddit_appKwargs)
        
        See :meth:`~.RedditAppHelper.create` for the required params.
        '''
        ## self.refresh_token = models.RefreshTokenHelper(self)
        '''An instance of :class:`.RefreshTokenHelper`.

        Provides the interface for interacting with :class:`.RefreshToken`.
        For example to get a ``refresh_token`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            refresh_token = credmgr.refresh_token(1)
            print(refresh_token.id)
        
        .. note::
            Refresh tokens cannot be manually created.
        '''
        ## self.user_verification = models.UserVerificationHelper(self)
        '''An instance of :class:`.UserVerificationHelper`.

        Provides the interface for interacting with :class:`.UserVerification`.
        For example to get a ``user_verification`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            user_verification = credmgr.user_verification(1)
            print(user_verification.id)
        
        To create a ``user_verification`` do:
        
        ..code-block:: python
            user_verification = credmgr.user_verification.create(**user_verificationKwargs)
        
        See :meth:`~.UserVerificationHelper.create` for the required params.
        '''
        ## self.sentry_token = models.SentryTokenHelper(self)
        '''An instance of :class:`.SentryTokenHelper`.

        Provides the interface for interacting with :class:`.SentryToken`.
        For example to get a ``sentry_token`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            sentry_token = credmgr.sentry_token(1)
            print(sentry_token.id)
        
        To create a ``sentry_token`` do:
        
        ..code-block:: python
            sentry_token = credmgr.sentry_token.create(**sentry_tokenKwargs)
        
        See :meth:`~.SentryTokenHelper.create` for the required params.
        '''
        ## self.database_credential = models.DatabaseCredentialHelper(self)
        '''An instance of :class:`.DatabaseCredentialHelper`.

        Provides the interface for interacting with :class:`.DatabaseCredential`.
        For example to get a ``database_credential`` with ``id`` of ``1`` do:
        
        .. code-block:: python
            database_credential = credmgr.database_credential(1)
            print(database_credential.id)
        
        To create a ``database_credential`` do:
        
        ..code-block:: python
            database_credential = credmgr.database_credential.create(**database_credentialKwargs)
        
        See :meth:`~.DatabaseCredentialHelper.create` for the required params.
        '''

    def api_tokens(self, owner_id=None, limit=10, offset=0):
        return ApiToken(self).list(limit=limit, offset=offset, owner_id=owner_id)

    def users(self, limit=10, offset=0):
        return User(self).list(limit=limit, offset=offset)

    def bots(self, owner_id=None, limit=10, offset=0):
        return Bot(self).list(limit=limit, offset=offset, owner_id=owner_id)

    def reddit_apps(self, owner_id=None, limit=10, offset=0):
        return RedditApp(self).list(limit=limit, offset=offset, owner_id=owner_id)

    def refresh_tokens(self, owner_id=None, limit=10, offset=0):
        return RefreshToken(self).list(limit=limit, offset=offset, owner_id=owner_id)

    def user_verifications(self, owner_id=None, limit=10, offset=0):
        return UserVerification(self).list(limit=limit, offset=offset, owner_id=owner_id)

    def sentry_tokens(self, owner_id=None, limit=10, offset=0):
        return SentryToken(self).list(limit=limit, offset=offset, owner_id=owner_id)

    def database_credentials(self, owner_id=None, limit=10, offset=0):
        return DatabaseCredential(self).list(limit=limit, offset=offset, owner_id=owner_id)

    def currentUser(self):
        return self.get('/users/me')

    def get(self, path, params=None):
        return self.serializer.deserialize(self._requestor.request(path, 'GET', params=params))

    def post(self, path, data):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return self.serializer.deserialize(self._requestor.request(path, 'POST', data=data, headers=headers))

    def patch(self, path, data):
        return self.serializer.deserialize(self._requestor.request(path, 'PATCH', json=data))

    def delete(self, path):
        return self._requestor.request(path, 'DELETE')