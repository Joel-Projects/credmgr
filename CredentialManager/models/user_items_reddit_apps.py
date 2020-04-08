import pprint
import re


class UserItemsRedditApps(object):

    _swagger_types = {
        'id': 'int', 'app_name': 'str', 'client_id': 'str', 'client_secret': 'str'
        }

    _attribute_map = {
        'id': 'id', 'app_name': 'app_name', 'client_id': 'client_id', 'client_secret': 'client_secret'
        }

    def __init__(self, id=None, app_name=None, client_id=None, client_secret=None):
        '''UserItemsRedditApps - a model defined in Swagger'''

        self._id = None
        self._app_name = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.app_name = app_name
        self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret

    @property
    def id(self):
        '''Gets the id of this UserItemsRedditApps.


        :return: The id of this UserItemsRedditApps.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this UserItemsRedditApps.


        :param id: The id of this UserItemsRedditApps.
        :type: int
        '''

        self._id = id

    @property
    def app_name(self):
        '''Gets the app_name of this UserItemsRedditApps.


        :return: The app_name of this UserItemsRedditApps.
        :rtype: str
        '''
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        '''Sets the app_name of this UserItemsRedditApps.


        :param app_name: The app_name of this UserItemsRedditApps.
        :type: str
        '''
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")

        self._app_name = app_name

    @property
    def client_id(self):
        '''Gets the client_id of this UserItemsRedditApps.


        :return: The client_id of this UserItemsRedditApps.
        :rtype: str
        '''
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        '''Sets the client_id of this UserItemsRedditApps.


        :param client_id: The client_id of this UserItemsRedditApps.
        :type: str
        '''
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def client_secret(self):
        '''Gets the client_secret of this UserItemsRedditApps.


        :return: The client_secret of this UserItemsRedditApps.
        :rtype: str
        '''
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        '''Sets the client_secret of this UserItemsRedditApps.


        :param client_secret: The client_secret of this UserItemsRedditApps.
        :type: str
        '''

        self._client_secret = client_secret

    def to_dict(self):
        '''Returns the model properties as a dict'''
        result = {}

        for attr, _ in self._swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value
        if issubclass(UserItemsRedditApps, dict):
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
        if not isinstance(other, UserItemsRedditApps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other