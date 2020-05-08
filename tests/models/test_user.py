import pytest

from credmgr.exceptions import Conflict, NotFound


data = {
    'username': 'username',
    'password': 'password',
    'redditUsername': 'redditUsername',
    'defaultSettings': {'database_flavor': 'postgres', 'user_agent': 'userAgent'}
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
    data = {'username': 'newUsername', 'redditUsername': 'newRedditUsername', 'defaultSettings': {'database_host': 'localhost', 'database_flavor': 'postgres', 'user_agent': 'userAgent'}}
    user.edit(**data)
    modifiedUser = credmgr.user('newUsername')
    for key, value in data.items():
        assert getattr(modifiedUser, key) == value

def testEditUserConflictingData(credmgr):
    user = credmgr.user(6)
    with pytest.raises(Conflict):
        user.edit(username='username')

def testListRedditApps(credmgr):
    users = credmgr.users()
    users = [i for i in users]
    assert isinstance(users, list)
