import pprint
import re


class UserItemsDatabaseCredentials(object):

    _attr_types = {
        'id': 'int', 'app_name': 'str', 'database_username': 'str', 'database_host': 'str', 'database': 'str', 'database_flavor': 'str'
        }

    _attribute_map = {
        'id': 'id',
        'app_name': 'app_name',
        'database_username': 'database_username',
        'database_host': 'database_host',
        'database': 'database',
        'database_flavor': 'database_flavor'
        }

    def __init__(self, id=None, app_name=None, database_username=None, database_host=None, database=None, database_flavor=None):
        '''UserItemsDatabaseCredentials - a model defined in Swagger'''

        self._id = None
        self._app_name = None
        self._database_username = None
        self._database_host = None
        self._database = None
        self._database_flavor = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.app_name = app_name
        self.database_username = database_username
        if database_host is not None:
            self.database_host = database_host
        if database is not None:
            self.database = database
        if database_flavor is not None:
            self.database_flavor = database_flavor

    @property
    def id(self):
        '''Gets the id of this UserItemsDatabaseCredentials.


        :return: The id of this UserItemsDatabaseCredentials.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this UserItemsDatabaseCredentials.


        :param id: The id of this UserItemsDatabaseCredentials.
        :type: int
        '''

        self._id = id

    @property
    def app_name(self):
        '''Gets the app_name of this UserItemsDatabaseCredentials.


        :return: The app_name of this UserItemsDatabaseCredentials.
        :rtype: str
        '''
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        '''Sets the app_name of this UserItemsDatabaseCredentials.


        :param app_name: The app_name of this UserItemsDatabaseCredentials.
        :type: str
        '''
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")

        self._app_name = app_name

    @property
    def database_username(self):
        '''Gets the database_username of this UserItemsDatabaseCredentials.


        :return: The database_username of this UserItemsDatabaseCredentials.
        :rtype: str
        '''
        return self._database_username

    @database_username.setter
    def database_username(self, database_username):
        '''Sets the database_username of this UserItemsDatabaseCredentials.


        :param database_username: The database_username of this UserItemsDatabaseCredentials.
        :type: str
        '''
        if database_username is None:
            raise ValueError("Invalid value for `database_username`, must not be `None`")

        self._database_username = database_username

    @property
    def database_host(self):
        '''Gets the database_host of this UserItemsDatabaseCredentials.


        :return: The database_host of this UserItemsDatabaseCredentials.
        :rtype: str
        '''
        return self._database_host

    @database_host.setter
    def database_host(self, database_host):
        '''Sets the database_host of this UserItemsDatabaseCredentials.


        :param database_host: The database_host of this UserItemsDatabaseCredentials.
        :type: str
        '''

        self._database_host = database_host

    @property
    def database(self):
        '''Gets the database of this UserItemsDatabaseCredentials.


        :return: The database of this UserItemsDatabaseCredentials.
        :rtype: str
        '''
        return self._database

    @database.setter
    def database(self, database):
        '''Sets the database of this UserItemsDatabaseCredentials.


        :param database: The database of this UserItemsDatabaseCredentials.
        :type: str
        '''

        self._database = database

    @property
    def database_flavor(self):
        '''Gets the database_flavor of this UserItemsDatabaseCredentials.


        :return: The database_flavor of this UserItemsDatabaseCredentials.
        :rtype: str
        '''
        return self._database_flavor

    @database_flavor.setter
    def database_flavor(self, database_flavor):
        '''Sets the database_flavor of this UserItemsDatabaseCredentials.


        :param database_flavor: The database_flavor of this UserItemsDatabaseCredentials.
        :type: str
        '''

        self._database_flavor = database_flavor

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
        if issubclass(UserItemsDatabaseCredentials, dict):
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
        if not isinstance(other, UserItemsDatabaseCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other