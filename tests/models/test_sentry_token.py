import praw
import pytest
from credmgr.models import SentryToken

from credmgr.exceptions import Conflict, NotFound, ServerError


def testCreateSentryToken(credentialManager):
    data = {'name': 'testSentryToken', 'dsn': 'https://key@sentry.jesassn.org/id'}
    sentryToken = credentialManager.sentryToken.create(**data)
    for key, value in data.items():
        assert getattr(sentryToken, key) == value

def testCreateSentryTokenOtherUser(credentialManager):
    data = {'name': 'testSentryToken', 'dsn': 'https://key@sentry.jesassn.org/id', 'owner': 4}
    sentryToken = credentialManager.sentryToken.create(**data)
    for key, value in data.items():
        if key == 'owner':
            assert getattr(sentryToken, key).id == value
            continue
        assert getattr(sentryToken, key) == value

def testCreateSentryTokenBadParams(credentialManager):
    data = {'name': 'se', 'dsn': 'https://key@sentry.jesassn.org/id2'}
    with pytest.raises(ServerError):
        _ = credentialManager.sentryToken.create(**data)

def testCreateSentryTokenExisting(credentialManager):
    data = {'name': 'sentryToken', 'dsn': 'https://key@sentry.jesassn.org/id'}
    with pytest.raises(Conflict):
        _ = credentialManager.sentryToken.create(**data)

def testDeleteSentryToken(credentialManager):
    sentryToken = credentialManager.sentryToken(1)
    sentryToken.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.sentryToken(1)

def testEditSentryToken(credentialManager):
    sentryToken = credentialManager.sentryToken(2)
    sentryToken.edit(dsn='https://key@sentry.jesassn.org/idNew')
    assert sentryToken.dsn == 'https://key@sentry.jesassn.org/idNew'

def testEditSentryTokenConflictingData(credentialManager):
    sentryToken = credentialManager.sentryToken(2)
    with pytest.raises(Conflict):
        sentryToken.edit(name='sentryToken')

def testListSentryTokens(credentialManager):
    sentryTokens = credentialManager.sentryTokens()
    for sentryToken in sentryTokens:
        assert isinstance(sentryToken, SentryToken)
