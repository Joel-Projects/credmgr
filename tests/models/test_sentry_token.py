import pytest

from credmgr.exceptions import Conflict, NotFound, ServerError
from credmgr.models import SentryToken


def testCreateSentryToken(recorder, credentialManager):
    data = {"name": "testSentryToken", "dsn": "https://key@sentry.jesassn.org/id"}
    sentryToken = credentialManager.sentryToken.create(**data)
    for key, value in data.items():
        assert getattr(sentryToken, key) == value


def testCreateSentryTokenOtherUser(recorder, credentialManager):
    data = {
        "name": "testSentryToken",
        "dsn": "https://key@sentry.jesassn.org/id",
        "owner": 4,
    }
    sentryToken = credentialManager.sentryToken.create(**data)
    for key, value in data.items():
        if key == "owner":
            assert getattr(sentryToken, key).id == value
            continue
        assert getattr(sentryToken, key) == value


def testCreateSentryTokenBadParams(recorder, credentialManager):
    data = {"name": "se", "dsn": "https://key@sentry.jesassn.org/id2"}
    with pytest.raises(ServerError):
        _ = credentialManager.sentryToken.create(**data)


def testCreateSentryTokenExisting(recorder, credentialManager):
    data = {"name": "sentryToken", "dsn": "https://key@sentry.jesassn.org/id"}
    with pytest.raises(Conflict):
        _ = credentialManager.sentryToken.create(**data)


def testDeleteSentryToken(recorder, credentialManager):
    sentryToken = credentialManager.sentryToken(1)
    sentryToken.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.sentryToken(1)


def testEditSentryToken(recorder, credentialManager):
    sentryToken = credentialManager.sentryToken(2)
    sentryToken.edit(dsn="https://key@sentry.jesassn.org/idNew")
    assert sentryToken.dsn == "https://key@sentry.jesassn.org/idNew"


def testEditSentryTokenConflictingData(recorder, credentialManager):
    sentryToken = credentialManager.sentryToken(2)
    with pytest.raises(Conflict):
        sentryToken.edit(name="sentryToken")


def testListSentryTokens(recorder, credentialManager):
    sentryTokens = credentialManager.sentryTokens()
    for sentryToken in sentryTokens:
        assert isinstance(sentryToken, SentryToken)
