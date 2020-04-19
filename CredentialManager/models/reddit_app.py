import base64

import praw
import requests

from .utils import resolveModelFromInput, resolveUser
from ..mixins import BaseApp


class RedditApp(BaseApp):
    _attrTypes = {
        **BaseApp._attrTypes,
        'client_id': 'str',
        'client_secret': 'str',
        'short_name': 'str',
        'app_description': 'str',
        'user_agent': 'str',
        'app_type': 'str',
        'redirect_uri': 'str',
        'state': 'str'
        }

    _editableAttrs = BaseApp._editableAttrs + ['client_id', 'client_secret', 'short_name', 'app_description', 'user_agent', 'app_type', 'redirect_uri']
    _path = '/reddit_apps'
    _credmgrCallable = 'reddit_app'

    def __init__(self, credmgr, id=None, app_name=None, client_id=None, client_secret=None, short_name=None, app_description=None, user_agent=None,
                 app_type=None, redirect_uri=None, state=None, enabled=None, owner_id=None):
        super(RedditApp, self).__init__(credmgr, id, app_name, enabled, owner_id)
        self.client_id = client_id
        self.client_secret = client_secret
        self.short_name = short_name
        self.app_description = app_description
        self.user_agent = user_agent
        self.app_type = app_type
        self.redirect_uri = redirect_uri
        self.state = state
        self.enabled = enabled
        self.owner_id = owner_id

    @staticmethod
    @resolveUser()
    def _create(_credmgr, app_name, client_id, user_agent, app_type, redirect_uri, client_secret, short_name, app_description, enabled, owner=None):
        '''Create a new Reddit App

        **PERMISSIONS: At least Active user is required.**   Reddit Apps are used for interacting with reddit

        :param str app_name: (required)
        :param str client_id: Client ID of the Reddit App (required)
        :param str user_agent: User agent used for requests to Reddit's API (required)
        :param str app_type: Type of the app. One of `web`, `installed`, or `script` (required)
        :param str redirect_uri: Redirect URI for Oauth2 flow. Defaults to user set redirect uri (required)
        :param str client_secret: Client secret of the Reddit App
        :param str short_name: Short name of the Reddit App
        :param str app_description: Description of the Reddit App
        :param bool enabled: Allows the app to be used
        :param int owner: Owner of the app. Requires Admin to create for other users.
        :return: RedditApp
        '''
        data = {'app_name': app_name, 'client_id': client_id, 'user_agent': user_agent, 'app_type': app_type, 'redirect_uri': redirect_uri}
        if client_secret:
            data['client_secret'] = client_secret
        if short_name:
            data['short_name'] = short_name
        if app_description:
            data['app_description'] = app_description
        if enabled:
            data['enabled'] = enabled
        if owner:
            data['owner_id'] = owner
        return _credmgr.post('/reddit_apps', data=data)

    @property
    def reddit(self) -> praw.reddit:
        return praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, user_agent=self.user_agent, redirect_uri=self.redirect_uri)

    def createAuthUrl(self, scopes=None, permanent=False, user_verification=None):
        '''

        :param Union[list,str] scopes: List of scopes needed. Pass ``'all'`` for all scopes. ``identity`` scope will always be included. (default: ``['identity']``)
        :param bool permanent: Determines if a refresh token will be provided
        :param Union[UserVerification,int,str] user_verification: Link to a :class:`.UserVerification` object
        '''
        from CredentialManager.models import UserVerification
        if scopes is None:
            scopes = ['identity']
        elif scopes == 'all':
            scopes = ['*']
        if not 'identity' in scopes and scopes != ['*']:
            scopes.append('identity')
        userVerification = resolveModelFromInput(self._credmgr, UserVerification, user_verification, 'user_id')
        if userVerification:
            state = base64.urlsafe_b64encode(f'{self.state}:{userVerification}'.encode()).encode()
        else:
            state = self.state
        return self.reddit.auth.url(scopes, state, permanent)