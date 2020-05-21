import pytest

from credmgr.exceptions import Conflict, InitializationError, NotFound
from credmgr.models import SentryToken, User


data = {
    'username': 'username', 'password': 'password', 'redditUsername': 'redditUsername', 'defaultSettings': {'database_flavor': 'postgres', 'user_agent': 'userAgent'}
}

def testCreateUser(credentialManager):
    data = {'username': 'username', 'password': 'password', 'redditUsername': 'redditUsername', 'defaultSettings': {'database_flavor': 'postgres', 'user_agent': 'userAgent'}}
    user = credentialManager.user.create(**data)
    data.pop('password')
    for key, value in data.items():
        assert getattr(user, key) == value

def testCreateUserBadParams(credentialManager):
    data = {'username': 'te'}
    with pytest.raises(TypeError):
        _ = credentialManager.user.create(**data)

def testCreateUserExisting(credentialManager):
    data = {'username': 'username', 'password': 'password'}
    with pytest.raises(Conflict):
        _ = credentialManager.user.create(**data)

def testDeleteUser(credentialManager):
    user = credentialManager.user(12)
    user.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.user(12)

def testEditUser(credentialManager):
    user = credentialManager.user('test2')
    data = {
        'username': 'newUsername',
        'redditUsername': 'newRedditUsername',
        'defaultSettings': {'database_host': 'localhost', 'database_flavor': 'postgres', 'user_agent': 'userAgent'}
    }
    user.edit(**data)
    modifiedUser = credentialManager.user('newUsername')
    for key, value in data.items():
        assert getattr(modifiedUser, key) == value

def testEditUserConflictingData(credentialManager):
    user = credentialManager.user(6)
    with pytest.raises(Conflict):
        user.edit(username='username')

def testListUsers(credentialManager):
    users = credentialManager.users()
    for user in users:
        assert isinstance(user, User)

def testListUsersWithUser(credentialManager):
    with pytest.raises(InitializationError):
        _ = credentialManager.user()

def testToDict(credentialManager):
    user = credentialManager.currentUser
    user.apps()
    exportDict = user.toDict()
    exportDict.pop('created')
    exportDict.pop('updated')
    assert exportDict == {
        'database_credentials': [{
            'app_name': 'test',
            'database': 'postgres',
            'database_flavor': 'postgres',
            'database_host': 'localhost',
            'database_password': 'postgres',
            'database_port': 5432,
            'database_username': 'postgres',
            'id': 1,
            'owner_id': 1,
            'ssh_port': 22
        }], 'default_settings': {
            'database_flavor': 'postgres', 'database_host': 'localhost'
        }, 'id': 1, 'is_active': True, 'is_regular_user': True, 'reddit_apps': [{
            'app_name': 'Test',
            'app_type': 'web',
            'client_id': 'client_id2',
            'client_secret': 'client_secret2',
            'id': 2,
            'owner_id': 1,
            'redirect_uri': 'https://credmgr.jesassn.org/oauth2/reddit_callback',
            'short_name': 'test',
            'state': 'state',
            'user_agent': 'nah'
        }], 'reddit_username': 'Lil_SpazJoekp', 'sentry_tokens': [{
            'app_name': 'sentryToken', 'dsn': 'https://key@sentry.jesassn.org/id', 'id': 4, 'owner_id': 1
        }], 'username': 'spaz'
    }

def testAppsOnly(credentialManager):
    user = credentialManager.currentUser
    sentryTokens = user.apps('sentryTokens')
    assert isinstance(sentryTokens, list)
    for token in sentryTokens:
        assert isinstance(token, SentryToken)

def testAppsOnlyInvalid(credentialManager):
    user = credentialManager.currentUser
    with pytest.raises(InitializationError):
        _ = user.apps('invalid')