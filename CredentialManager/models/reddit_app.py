from ..mixins import BaseApp

class RedditApp(BaseApp):

    _attr_types = {**BaseApp._attr_types,
        'client_id': 'str',
        'client_secret': 'str',
        'short_name': 'str',
        'app_description': 'str',
        'user_agent': 'str',
        'app_type': 'str',
        'redirect_uri': 'str',
        'state': 'str'
        }

    _attribute_map = {**BaseApp._attribute_map,
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'short_name': 'short_name',
        'app_description': 'app_description',
        'user_agent': 'user_agent',
        'app_type': 'app_type',
        'redirect_uri': 'redirect_uri',
        'state': 'state'
        }
    editableAttrs = BaseApp._editableAttrs + [
        'client_id',
        'client_secret',
        'short_name',
        'app_description',
        'user_agent',
        'app_type',
        'redirect_uri'
        ]
    _path = '/reddit_apps'
    def __init__(self, credmgr, id=None, app_name=None, client_id=None, client_secret=None, short_name=None, app_description=None, user_agent=None, app_type=None, redirect_uri=None, state=None, enabled=None, owner_id=None):
        super(RedditApp, self).__init__(credmgr, id, app_name, enabled, owner_id)
        if client_id:
            self.client_id = client_id
        if client_secret:
            self.client_secret = client_secret
        if short_name:
            self.short_name = short_name
        if app_description:
            self.app_description = app_description
        if user_agent:
            self.user_agent = user_agent
        if app_type:
            self.app_type = app_type
        if redirect_uri:
            self.redirect_uri = redirect_uri
        if state:
            self.state = state
        if enabled:
            self.enabled = enabled
        if owner_id:
            self.owner_id = owner_id