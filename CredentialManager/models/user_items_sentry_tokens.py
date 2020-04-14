import pprint
import re


class UserItemsSentryTokens(object):

    _attr_types = {
        'id': 'int', 'app_name': 'str', 'dsn': 'str', 'enabled': 'bool'
        }

    _attribute_map = {
        'id': 'id', 'app_name': 'app_name', 'dsn': 'dsn', 'enabled': 'enabled'
        }

    def __init__(self, id=None, app_name=None, dsn=None, enabled=None):
        '''UserItemsSentryTokens - a model defined in Swagger'''

        self._id = None
        self._app_name = None
        self._dsn = None
        self._enabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if app_name is not None:
            self.app_name = app_name
        self.dsn = dsn
        if enabled is not None:
            self.enabled = enabled

    @property
    def id(self):
        '''Gets the id of this UserItemsSentryTokens.


        :return: The id of this UserItemsSentryTokens.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this UserItemsSentryTokens.


        :param id: The id of this UserItemsSentryTokens.
        :type: int
        '''

        self._id = id

    @property
    def app_name(self):
        '''Gets the app_name of this UserItemsSentryTokens.


        :return: The app_name of this UserItemsSentryTokens.
        :rtype: str
        '''
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        '''Sets the app_name of this UserItemsSentryTokens.


        :param app_name: The app_name of this UserItemsSentryTokens.
        :type: str
        '''

        self._app_name = app_name

    @property
    def dsn(self):
        '''Gets the dsn of this UserItemsSentryTokens.


        :return: The dsn of this UserItemsSentryTokens.
        :rtype: str
        '''
        return self._dsn

    @dsn.setter
    def dsn(self, dsn):
        '''Sets the dsn of this UserItemsSentryTokens.


        :param dsn: The dsn of this UserItemsSentryTokens.
        :type: str
        '''
        if dsn is None:
            raise ValueError("Invalid value for `dsn`, must not be `None`")

        self._dsn = dsn

    @property
    def enabled(self):
        '''Gets the enabled of this UserItemsSentryTokens.


        :return: The enabled of this UserItemsSentryTokens.
        :rtype: bool
        '''
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        '''Sets the enabled of this UserItemsSentryTokens.


        :param enabled: The enabled of this UserItemsSentryTokens.
        :type: bool
        '''

        self._enabled = enabled

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
        if issubclass(UserItemsSentryTokens, dict):
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
        if not isinstance(other, UserItemsSentryTokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other