import pytest

from credmgr.exceptions import Conflict, NotFound
from credmgr.models import UserVerification


def testCreateUserVerification(recorder, credentialManager):
    data = {"userId": "12345", "redditApp": 27}
    userVerification = credentialManager.userVerification.create(**data)
    for key, value in data.items():
        if key == "redditApp":
            assert getattr(userVerification, key).id == value
            continue
        assert getattr(userVerification, key) == value


def testCreateUserVerificationFullParams(recorder, credentialManager):
    data = {
        "userId": "1234567",
        "redditApp": 27,
        "redditor": "redditor",
        "extraData": {"extra": "data", "nested": {"dict": "value"}},
    }
    userVerification = credentialManager.userVerification.create(**data)
    for key, value in data.items():
        if key == "redditApp":
            assert getattr(userVerification, key).id == value
            continue
        assert getattr(userVerification, key) == value


def testCreateUserVerificationOtherUser(recorder, credentialManager):
    data = {"userId": "123456", "redditApp": 22, "owner": 4}
    userVerification = credentialManager.userVerification.create(**data)
    for key, value in data.items():
        if key in ["owner", "redditApp"]:
            assert getattr(userVerification, key).id == value
            continue
        assert getattr(userVerification, key) == value


def testCreateUserVerificationExisting(recorder, credentialManager):
    data = {"userId": "12345", "redditApp": 27}
    existing = credentialManager.userVerification.create(**data)
    assert isinstance(existing, UserVerification)
    assert existing.userId == "12345"


def testDeleteUserVerification(recorder, credentialManager):
    userVerification = credentialManager.userVerification("12345")
    userVerification.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.userVerification("12345")


def testEditUserVerification(recorder, credentialManager):
    userVerification = credentialManager.userVerification("newId")
    userVerification.edit(redditor="redditor")
    assert userVerification.redditor == "redditor"


def testEditUserVerificationConflictingData(recorder, credentialManager):
    userVerification = credentialManager.userVerification("newId")
    with pytest.raises(Conflict):
        userVerification.edit(userId="12345")


def testListUserVerifications(recorder, credentialManager):
    userVerifications = credentialManager.userVerifications()
    for userVerification in userVerifications:
        assert isinstance(userVerification, UserVerification)
