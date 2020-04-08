import pprint
import re


class UserItems(object):

    _swagger_types = {
        'id': 'int',
        'username': 'str',
        'reddit_apps': 'list[UserItemsRedditApps]',
        'sentry_tokens': 'list[UserItemsSentryTokens]',
        'database_credentials': 'list[UserItemsDatabaseCredentials]',
        'created': 'datetime',
        'updated': 'datetime'
        }

    _attribute_map = {
        'id': 'id',
        'username': 'username',
        'reddit_apps': 'reddit_apps',
        'sentry_tokens': 'sentry_tokens',
        'database_credentials': 'database_credentials',
        'created': 'created',
        'updated': 'updated'
        }

    def __init__(self, id=None, username=None, reddit_apps=None, sentry_tokens=None, database_credentials=None, created=None, updated=None):
        '''UserItems - a model defined in Swagger'''

        self._id = None
        self._username = None
        self._reddit_apps = None
        self._sentry_tokens = None
        self._database_credentials = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.username = username
        if reddit_apps is not None:
            self.reddit_apps = reddit_apps
        if sentry_tokens is not None:
            self.sentry_tokens = sentry_tokens
        if database_credentials is not None:
            self.database_credentials = database_credentials
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        '''Gets the id of this UserItems.


        :return: The id of this UserItems.
        :rtype: int
        '''
        return self._id

    @id.setter
    def id(self, id):
        '''Sets the id of this UserItems.


        :param id: The id of this UserItems.
        :type: int
        '''

        self._id = id

    @property
    def username(self):
        '''Gets the username of this UserItems.


        :return: The username of this UserItems.
        :rtype: str
        '''
        return self._username

    @username.setter
    def username(self, username):
        '''Sets the username of this UserItems.


        :param username: The username of this UserItems.
        :type: str
        '''
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")
        if username is not None and len(username) > 80:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `80`")

        self._username = username

    @property
    def reddit_apps(self):
        '''Gets the reddit_apps of this UserItems.


        :return: The reddit_apps of this UserItems.
        :rtype: list[UserItemsRedditApps]
        '''
        return self._reddit_apps

    @reddit_apps.setter
    def reddit_apps(self, reddit_apps):
        '''Sets the reddit_apps of this UserItems.


        :param reddit_apps: The reddit_apps of this UserItems.
        :type: list[UserItemsRedditApps]
        '''

        self._reddit_apps = reddit_apps

    @property
    def sentry_tokens(self):
        '''Gets the sentry_tokens of this UserItems.


        :return: The sentry_tokens of this UserItems.
        :rtype: list[UserItemsSentryTokens]
        '''
        return self._sentry_tokens

    @sentry_tokens.setter
    def sentry_tokens(self, sentry_tokens):
        '''Sets the sentry_tokens of this UserItems.


        :param sentry_tokens: The sentry_tokens of this UserItems.
        :type: list[UserItemsSentryTokens]
        '''

        self._sentry_tokens = sentry_tokens

    @property
    def database_credentials(self):
        '''Gets the database_credentials of this UserItems.


        :return: The database_credentials of this UserItems.
        :rtype: list[UserItemsDatabaseCredentials]
        '''
        return self._database_credentials

    @database_credentials.setter
    def database_credentials(self, database_credentials):
        '''Sets the database_credentials of this UserItems.


        :param database_credentials: The database_credentials of this UserItems.
        :type: list[UserItemsDatabaseCredentials]
        '''

        self._database_credentials = database_credentials

    @property
    def created(self):
        '''Gets the created of this UserItems.


        :return: The created of this UserItems.
        :rtype: datetime
        '''
        return self._created

    @created.setter
    def created(self, created):
        '''Sets the created of this UserItems.


        :param created: The created of this UserItems.
        :type: datetime
        '''

        self._created = created

    @property
    def updated(self):
        '''Gets the updated of this UserItems.


        :return: The updated of this UserItems.
        :rtype: datetime
        '''
        return self._updated

    @updated.setter
    def updated(self, updated):
        '''Sets the updated of this UserItems.


        :param updated: The updated of this UserItems.
        :type: datetime
        '''

        self._updated = updated

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
        if issubclass(UserItems, dict):
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
        if not isinstance(other, UserItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        '''Returns true if both objects are not equal'''
        return not self == other