import pprint
import re


class BotRedditApp(object):

    _attr_types = {
        'id': 'int', 'app_name': 'str', 'client_id': 'str', 'client_secret': 'str', 'user_agent': 'str', 'redirect_uri': 'str'
        }

    _attribute_map = {
        'id': 'id',
        'app_name': 'app_name',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'user_agent': 'user_agent',
        'redirect_uri': 'redirect_uri'
        }

    def __init__(self, id=None, app_name=None, client_id=None, client_secret=None, user_agent=None, redirect_uri=None):
        '''BotRedditApp - a model defined in Swagger'''

        self._id = None
        self._app_name = None
        self._client_id = None
        self._client_secret = None
        self._user_agent = None
        self._redirect_uri = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.app_name = app_name
        self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        self.user_agent = user_agent
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri

    @property
    def id(self):
        '''Gets the id of this BotRedditApp.


        :return: The id of this BotRedditApp.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this BotRedditApp.


        :param id: The id of this BotRedditApp.
        :type: int
        '''

        self._id = id

    @property
    def app_name(self):
        '''Gets the app_name of this BotRedditApp.


        :return: The app_name of this BotRedditApp.
        :rtype: str
        '''
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        '''Sets the app_name of this BotRedditApp.


        :param app_name: The app_name of this BotRedditApp.
        :type: str
        '''
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")

        self._app_name = app_name

    @property
    def client_id(self):
        '''Gets the client_id of this BotRedditApp.


        :return: The client_id of this BotRedditApp.
        :rtype: str
        '''
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        '''Sets the client_id of this BotRedditApp.


        :param client_id: The client_id of this BotRedditApp.
        :type: str
        '''
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def client_secret(self):
        '''Gets the client_secret of this BotRedditApp.


        :return: The client_secret of this BotRedditApp.
        :rtype: str
        '''
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        '''Sets the client_secret of this BotRedditApp.


        :param client_secret: The client_secret of this BotRedditApp.
        :type: str
        '''

        self._client_secret = client_secret

    @property
    def user_agent(self):
        '''Gets the user_agent of this BotRedditApp.


        :return: The user_agent of this BotRedditApp.
        :rtype: str
        '''
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        '''Sets the user_agent of this BotRedditApp.


        :param user_agent: The user_agent of this BotRedditApp.
        :type: str
        '''
        if user_agent is None:
            raise ValueError("Invalid value for `user_agent`, must not be `None`")

        self._user_agent = user_agent

    @property
    def redirect_uri(self):
        '''Gets the redirect_uri of this BotRedditApp.


        :return: The redirect_uri of this BotRedditApp.
        :rtype: str
        '''
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        '''Sets the redirect_uri of this BotRedditApp.


        :param redirect_uri: The redirect_uri of this BotRedditApp.
        :type: str
        '''

        self._redirect_uri = redirect_uri

    def to_dict(self):
        '''Returns the model properties as a dict'''
        result = {}

        for attr, _ in self._attr_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value
        if issubclass(BotRedditApp, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        '''Returns the string representation of the model'''
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        '''For `print` and `pprint`'''
        return self.to_str()

    def __eq__(self, other):
        '''Returns true if both objects are equal'''
        if not isinstance(other, BotRedditApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other