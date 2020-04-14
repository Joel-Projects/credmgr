import pprint
import re


class AuthUrl(object):

    _attr_types = {
        'id': 'int', 'app_name': 'str', 'client_id': 'str', 'auth_url': 'str'
        }

    _attribute_map = {
        'id': 'id', 'app_name': 'app_name', 'client_id': 'client_id', 'auth_url': 'auth_url'
        }

    def __init__(self, id=None, app_name=None, client_id=None, auth_url=None):
        '''AuthUrl - a model defined in Swagger'''

        self._id = None
        self._app_name = None
        self._client_id = None
        self._auth_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.app_name = app_name
        self.client_id = client_id
        if auth_url is not None:
            self.auth_url = auth_url

    @property
    def id(self):
        '''Gets the id of this AuthUrl.


        :return: The id of this AuthUrl.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this AuthUrl.


        :param id: The id of this AuthUrl.
        :type: int
        '''

        self._id = id

    @property
    def app_name(self):
        '''Gets the app_name of this AuthUrl.


        :return: The app_name of this AuthUrl.
        :rtype: str
        '''
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        '''Sets the app_name of this AuthUrl.


        :param app_name: The app_name of this AuthUrl.
        :type: str
        '''
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")

        self._app_name = app_name

    @property
    def client_id(self):
        '''Gets the client_id of this AuthUrl.


        :return: The client_id of this AuthUrl.
        :rtype: str
        '''
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        '''Sets the client_id of this AuthUrl.


        :param client_id: The client_id of this AuthUrl.
        :type: str
        '''
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def auth_url(self):
        '''Gets the auth_url of this AuthUrl.


        :return: The auth_url of this AuthUrl.
        :rtype: str
        '''
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        '''Sets the auth_url of this AuthUrl.


        :param auth_url: The auth_url of this AuthUrl.
        :type: str
        '''

        self._auth_url = auth_url

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
        if issubclass(AuthUrl, dict):
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
        if not isinstance(other, AuthUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other