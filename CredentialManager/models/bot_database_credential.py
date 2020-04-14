import pprint
import re


class BotDatabaseCredential(object):

    _attr_types = {
        'id': 'int',
        'app_name': 'str',
        'database_username': 'str',
        'database_host': 'str',
        'database': 'str',
        'database_flavor': 'str',
        'database_port': 'int',
        'database_password': 'str',
        'use_ssh': 'bool',
        'ssh_host': 'str',
        'ssh_port': 'int',
        'ssh_username': 'str',
        'ssh_password': 'str',
        'use_ssh_key': 'bool',
        'private_key': 'str',
        'private_key_passphrase': 'str'
        }

    _attribute_map = {
        'id': 'id',
        'app_name': 'app_name',
        'database_username': 'database_username',
        'database_host': 'database_host',
        'database': 'database',
        'database_flavor': 'database_flavor',
        'database_port': 'database_port',
        'database_password': 'database_password',
        'use_ssh': 'use_ssh',
        'ssh_host': 'ssh_host',
        'ssh_port': 'ssh_port',
        'ssh_username': 'ssh_username',
        'ssh_password': 'ssh_password',
        'use_ssh_key': 'use_ssh_key',
        'private_key': 'private_key',
        'private_key_passphrase': 'private_key_passphrase'
        }

    def __init__(self, id=None, app_name=None, database_username=None, database_host=None, database=None, database_flavor=None, database_port=None,
                 database_password=None, use_ssh=None, ssh_host=None, ssh_port=None, ssh_username=None, ssh_password=None, use_ssh_key=None,
                 private_key=None, private_key_passphrase=None):
        '''BotDatabaseCredential - a model defined in Swagger'''

        self._id = None
        self._app_name = None
        self._database_username = None
        self._database_host = None
        self._database = None
        self._database_flavor = None
        self._database_port = None
        self._database_password = None
        self._use_ssh = None
        self._ssh_host = None
        self._ssh_port = None
        self._ssh_username = None
        self._ssh_password = None
        self._use_ssh_key = None
        self._private_key = None
        self._private_key_passphrase = None
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
        if database_port is not None:
            self.database_port = database_port
        if database_password is not None:
            self.database_password = database_password
        if use_ssh is not None:
            self.use_ssh = use_ssh
        if ssh_host is not None:
            self.ssh_host = ssh_host
        if ssh_port is not None:
            self.ssh_port = ssh_port
        if ssh_username is not None:
            self.ssh_username = ssh_username
        if ssh_password is not None:
            self.ssh_password = ssh_password
        if use_ssh_key is not None:
            self.use_ssh_key = use_ssh_key
        if private_key is not None:
            self.private_key = private_key
        if private_key_passphrase is not None:
            self.private_key_passphrase = private_key_passphrase

    @property
    def id(self):
        '''Gets the id of this BotDatabaseCredential.


        :return: The id of this BotDatabaseCredential.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this BotDatabaseCredential.


        :param id: The id of this BotDatabaseCredential.
        :type: int
        '''

        self._id = id

    @property
    def app_name(self):
        '''Gets the app_name of this BotDatabaseCredential.


        :return: The app_name of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        '''Sets the app_name of this BotDatabaseCredential.


        :param app_name: The app_name of this BotDatabaseCredential.
        :type: str
        '''
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")

        self._app_name = app_name

    @property
    def database_username(self):
        '''Gets the database_username of this BotDatabaseCredential.


        :return: The database_username of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._database_username

    @database_username.setter
    def database_username(self, database_username):
        '''Sets the database_username of this BotDatabaseCredential.


        :param database_username: The database_username of this BotDatabaseCredential.
        :type: str
        '''
        if database_username is None:
            raise ValueError("Invalid value for `database_username`, must not be `None`")

        self._database_username = database_username

    @property
    def database_host(self):
        '''Gets the database_host of this BotDatabaseCredential.


        :return: The database_host of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._database_host

    @database_host.setter
    def database_host(self, database_host):
        '''Sets the database_host of this BotDatabaseCredential.


        :param database_host: The database_host of this BotDatabaseCredential.
        :type: str
        '''

        self._database_host = database_host

    @property
    def database(self):
        '''Gets the database of this BotDatabaseCredential.


        :return: The database of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._database

    @database.setter
    def database(self, database):
        '''Sets the database of this BotDatabaseCredential.


        :param database: The database of this BotDatabaseCredential.
        :type: str
        '''

        self._database = database

    @property
    def database_flavor(self):
        '''Gets the database_flavor of this BotDatabaseCredential.


        :return: The database_flavor of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._database_flavor

    @database_flavor.setter
    def database_flavor(self, database_flavor):
        '''Sets the database_flavor of this BotDatabaseCredential.


        :param database_flavor: The database_flavor of this BotDatabaseCredential.
        :type: str
        '''

        self._database_flavor = database_flavor

    @property
    def database_port(self):
        '''Gets the database_port of this BotDatabaseCredential.


        :return: The database_port of this BotDatabaseCredential.
        :rtype: int
        '''
        return self._database_port

    @database_port.setter
    def database_port(self, database_port):
        '''Sets the database_port of this BotDatabaseCredential.


        :param database_port: The database_port of this BotDatabaseCredential.
        :type: int
        '''

        self._database_port = database_port

    @property
    def database_password(self):
        '''Gets the database_password of this BotDatabaseCredential.


        :return: The database_password of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._database_password

    @database_password.setter
    def database_password(self, database_password):
        '''Sets the database_password of this BotDatabaseCredential.


        :param database_password: The database_password of this BotDatabaseCredential.
        :type: str
        '''

        self._database_password = database_password

    @property
    def use_ssh(self):
        '''Gets the use_ssh of this BotDatabaseCredential.


        :return: The use_ssh of this BotDatabaseCredential.
        :rtype: bool
        '''
        return self._use_ssh

    @use_ssh.setter
    def use_ssh(self, use_ssh):
        '''Sets the use_ssh of this BotDatabaseCredential.


        :param use_ssh: The use_ssh of this BotDatabaseCredential.
        :type: bool
        '''

        self._use_ssh = use_ssh

    @property
    def ssh_host(self):
        '''Gets the ssh_host of this BotDatabaseCredential.


        :return: The ssh_host of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._ssh_host

    @ssh_host.setter
    def ssh_host(self, ssh_host):
        '''Sets the ssh_host of this BotDatabaseCredential.


        :param ssh_host: The ssh_host of this BotDatabaseCredential.
        :type: str
        '''

        self._ssh_host = ssh_host

    @property
    def ssh_port(self):
        '''Gets the ssh_port of this BotDatabaseCredential.


        :return: The ssh_port of this BotDatabaseCredential.
        :rtype: int
        '''
        return self._ssh_port

    @ssh_port.setter
    def ssh_port(self, ssh_port):
        '''Sets the ssh_port of this BotDatabaseCredential.


        :param ssh_port: The ssh_port of this BotDatabaseCredential.
        :type: int
        '''

        self._ssh_port = ssh_port

    @property
    def ssh_username(self):
        '''Gets the ssh_username of this BotDatabaseCredential.


        :return: The ssh_username of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._ssh_username

    @ssh_username.setter
    def ssh_username(self, ssh_username):
        '''Sets the ssh_username of this BotDatabaseCredential.


        :param ssh_username: The ssh_username of this BotDatabaseCredential.
        :type: str
        '''

        self._ssh_username = ssh_username

    @property
    def ssh_password(self):
        '''Gets the ssh_password of this BotDatabaseCredential.


        :return: The ssh_password of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._ssh_password

    @ssh_password.setter
    def ssh_password(self, ssh_password):
        '''Sets the ssh_password of this BotDatabaseCredential.


        :param ssh_password: The ssh_password of this BotDatabaseCredential.
        :type: str
        '''

        self._ssh_password = ssh_password

    @property
    def use_ssh_key(self):
        '''Gets the use_ssh_key of this BotDatabaseCredential.


        :return: The use_ssh_key of this BotDatabaseCredential.
        :rtype: bool
        '''
        return self._use_ssh_key

    @use_ssh_key.setter
    def use_ssh_key(self, use_ssh_key):
        '''Sets the use_ssh_key of this BotDatabaseCredential.


        :param use_ssh_key: The use_ssh_key of this BotDatabaseCredential.
        :type: bool
        '''

        self._use_ssh_key = use_ssh_key

    @property
    def private_key(self):
        '''Gets the private_key of this BotDatabaseCredential.


        :return: The private_key of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        '''Sets the private_key of this BotDatabaseCredential.


        :param private_key: The private_key of this BotDatabaseCredential.
        :type: str
        '''

        self._private_key = private_key

    @property
    def private_key_passphrase(self):
        '''Gets the private_key_passphrase of this BotDatabaseCredential.


        :return: The private_key_passphrase of this BotDatabaseCredential.
        :rtype: str
        '''
        return self._private_key_passphrase

    @private_key_passphrase.setter
    def private_key_passphrase(self, private_key_passphrase):
        '''Sets the private_key_passphrase of this BotDatabaseCredential.


        :param private_key_passphrase: The private_key_passphrase of this BotDatabaseCredential.
        :type: str
        '''

        self._private_key_passphrase = private_key_passphrase

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
        if issubclass(BotDatabaseCredential, dict):
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
        if not isinstance(other, BotDatabaseCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other