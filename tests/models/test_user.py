import datetime

import pytest
from credmgr.models import SentryToken, User

from credmgr.exceptions import Conflict, InitializationError, NotFound


data = {
    'username': 'username', 'password': 'password', 'redditUsername': 'redditUsername', 'defaultSettings': {'database_flavor': 'postgres', 'user_agent': 'userAgent'}
}

def testCreateUser(credmgr):
    data = {'username': 'username', 'password': 'password', 'redditUsername': 'redditUsername', 'defaultSettings': {'database_flavor': 'postgres', 'user_agent': 'userAgent'}}
    user = credmgr.user.create(**data)
    data.pop('password')
    for key, value in data.items():
        assert getattr(user, key) == value

def testCreateUserBadParams(credmgr):
    data = {'username': 'te'}
    with pytest.raises(TypeError):
        _ = credmgr.user.create(**data)

def testCreateUserExisting(credmgr):
    data = {'username': 'username', 'password': 'password'}
    with pytest.raises(Conflict):
        _ = credmgr.user.create(**data)

def testDeleteUser(credmgr):
    user = credmgr.user(12)
    user.delete()
    with pytest.raises(NotFound):
        _ = credmgr.user(12)

def testEditUser(credmgr):
    user = credmgr.user('test2')
    data = {
        'username': 'newUsername',
        'redditUsername': 'newRedditUsername',
        'defaultSettings': {'database_host': 'localhost', 'database_flavor': 'postgres', 'user_agent': 'userAgent'}
    }
    user.edit(**data)
    modifiedUser = credmgr.user('newUsername')
    for key, value in data.items():
        assert getattr(modifiedUser, key) == value

def testEditUserConflictingData(credmgr):
    user = credmgr.user(6)
    with pytest.raises(Conflict):
        user.edit(username='username')

def testListUsers(credmgr):
    users = credmgr.users()
    for user in users:
        assert isinstance(user, User)

def testListUsersWithUser(credmgr):
    users = credmgr.user()
    for user in users:
        assert isinstance(user, User)

def testToDict(credmgr):
    user = credmgr.currentUser
    user.apps()
    exportDict = user.toDict()
    exportDict.pop('created')
    exportDict.pop('updated')
    assert exportDict == {
        'id': 1,
        'username': 'spaz',
        'is_active': True,
        'is_regular_user': True,
        'is_admin': True,
        'default_settings': {'database_flavor': 'postgres', 'database_host': 'localhost'},
        'reddit_username': 'Lil_SpazJoekp',
        'reddit_apps': [{'id': 22, 'app_name': 'testRedditApp', 'client_id': 'clientId', 'client_secret': 'clientSecret'},
                        {'id': 2, 'app_name': 'Test', 'client_id': 'client_id2', 'client_secret': 'client_secret2'}],
        'sentry_tokens': [{'id': 4, 'app_name': 'sentryToken', 'enabled': True, 'owner_id': 1, 'dsn': 'https://key@sentry.jesassn.org/id'}],
        'database_credentials': [{
            'id': 1,
            'app_name': 'test',
            'database_username': 'postgres',
            'database_host': 'localhost',
            'database': 'postgres',
            'database_flavor': 'postgres',
            'database_password': 'postgres',
            'ssh_port': 22
        }]
    }

def testAppsOnly(credmgr):
    user = credmgr.currentUser
    sentryTokens = user.apps('sentryTokens')
    assert isinstance(sentryTokens, list)
    for token in sentryTokens:
        assert isinstance(token, SentryToken)


def testAppsOnlyInvalid(credmgr):
    user = credmgr.currentUser
    with pytest.raises(InitializationError):
        _ = user.apps('invalid')