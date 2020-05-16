import pytest

from credmgr.exceptions import Conflict, NotFound
from credmgr.models import UserVerification


def testCreateUserVerification(credmgr):
    data = {'userId': '12345', 'redditApp': 22}
    userVerification = credmgr.userVerification.create(**data)
    for key, value in data.items():
        if key == 'redditApp':
            assert getattr(userVerification, key).id == value
            continue
        assert getattr(userVerification, key) == value

def testCreateUserVerificationFullParams(credmgr):
    data = {'userId': '1234567', 'redditApp': 22, 'redditor': 'redditor', 'extraData': {'extra': 'data', 'nested': {'dict': 'value'}}}
    userVerification = credmgr.userVerification.create(**data)
    for key, value in data.items():
        if key == 'redditApp':
            assert getattr(userVerification, key).id == value
            continue
        assert getattr(userVerification, key) == value

def testCreateUserVerificationOtherUser(credmgr):
    data = {'userId': '123456', 'redditApp': 22, 'owner': 4}
    userVerification = credmgr.userVerification.create(**data)
    for key, value in data.items():
        if key in ['owner', 'redditApp']:
            assert getattr(userVerification, key).id == value
            continue
        assert getattr(userVerification, key) == value

def testCreateUserVerificationExisting(credmgr):
    data = {'userId': '12345', 'redditApp': 27}
    existing = credmgr.userVerification.create(**data)
    assert isinstance(existing, UserVerification)
    assert existing.userId == '12345'

def testDeleteUserVerification(credmgr):
    userVerification = credmgr.userVerification('12345')
    userVerification.delete()
    with pytest.raises(NotFound):
        _ = credmgr.userVerification('12345')

def testEditUserVerification(credmgr):
    userVerification = credmgr.userVerification('newId')
    userVerification.edit(redditor='redditor')
    assert userVerification.redditor == 'redditor'

def testEditUserVerificationConflictingData(credmgr):
    userVerification = credmgr.userVerification('newId')
    with pytest.raises(Conflict):
        userVerification.edit(userId='12345')

def testListUserVerifications(credmgr):
    userVerifications = credmgr.userVerifications()
    for userVerification in userVerifications:
        assert isinstance(userVerification, UserVerification)

def testListUserVerificationsWithUserVerification(credmgr):
    userVerifications = credmgr.userVerification()
    for userVerification in userVerifications:
        assert isinstance(userVerification, UserVerification)