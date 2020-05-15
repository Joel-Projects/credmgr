import praw
import pytest
from credmgr.models import SentryToken

from credmgr.exceptions import Conflict, NotFound, ServerError


def testCreateSentryToken(credmgr):
    data = {'appName': 'testSentryToken', 'dsn': 'https://key@sentry.jesassn.org/id'}
    sentryToken = credmgr.sentryToken.create(**data)
    for key, value in data.items():
        assert getattr(sentryToken, key) == value

def testCreateSentryTokenOtherUser(credmgr):
    data = {'appName': 'testSentryToken', 'dsn': 'https://key@sentry.jesassn.org/id', 'owner': 4}
    sentryToken = credmgr.sentryToken.create(**data)
    for key, value in data.items():
        if key == 'owner':
            assert getattr(sentryToken, key).id == value
            continue
        assert getattr(sentryToken, key) == value

def testCreateSentryTokenBadParams(credmgr):
    data = {'appName': 'se', 'dsn': 'https://key@sentry.jesassn.org/id2'}
    with pytest.raises(ServerError):
        _ = credmgr.sentryToken.create(**data)

def testCreateSentryTokenExisting(credmgr):
    data = {'appName': 'sentryToken', 'dsn': 'https://key@sentry.jesassn.org/id'}
    with pytest.raises(Conflict):
        _ = credmgr.sentryToken.create(**data)

def testDeleteSentryToken(credmgr):
    sentryToken = credmgr.sentryToken(1)
    sentryToken.delete()
    with pytest.raises(NotFound):
        _ = credmgr.sentryToken(1)

def testEditSentryToken(credmgr):
    sentryToken = credmgr.sentryToken(2)
    sentryToken.edit(dsn='https://key@sentry.jesassn.org/idNew')
    assert sentryToken.dsn == 'https://key@sentry.jesassn.org/idNew'

def testEditSentryTokenConflictingData(credmgr):
    sentryToken = credmgr.sentryToken(2)
    with pytest.raises(Conflict):
        sentryToken.edit(appName='sentryToken')

def testListSentryTokens(credmgr):
    sentryTokens = credmgr.sentryTokens()
    for sentryToken in sentryTokens:
        assert isinstance(sentryToken, SentryToken)
