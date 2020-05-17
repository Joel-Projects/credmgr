import pytest
from credmgr.exceptions import InitializationError


def testUserHelperGetByID(credmgr):
    user = credmgr.user(1)
    assert getattr(user, user._nameAttr) == 'spaz'

def testUserHelperGetByName(credmgr):
    user = credmgr.user('spaz')
    assert getattr(user, user._nameAttr) == 'spaz'

def testUserVerificationHelperGetByID(credmgr):
    userVerification = credmgr.userVerification('0123456789')
    assert getattr(userVerification, userVerification._nameAttr) == '0123456789'

def testUserVerificationHelperGetByName(credmgr):
    data = {'userId': '123456', 'redditAppId': 22}
    userVerification = credmgr.userVerification(**data)
    for key, value in data.items():
        assert getattr(userVerification, key) == value

def testRefreshTokenHelperGetByID(credmgr):
    refreshToken = credmgr.refreshToken(redditor='Lil_SpazJoekp', redditAppId=2)
    assert getattr(refreshToken, refreshToken._nameAttr) == 'Lil_SpazJoekp'

def testRefreshTokenHelperGetByName(credmgr):
    data = {'redditor': 'Lil_SpazJoekp', 'redditAppId': 2}
    refreshToken = credmgr.refreshToken(**data)
    for key, value in data.items():
        assert getattr(refreshToken, key) == value

def testSentryTokenHelperGetByID(credmgr):
    sentryToken = credmgr.sentryToken(1)
    assert getattr(sentryToken, sentryToken._nameAttr) == 'test'

def testRedditAppHelperGetByID(credmgr):
    redditApp = credmgr.redditApp(1)
    assert getattr(redditApp, redditApp._nameAttr) == 'DankMemesModAbuse'

def testDatabaseCredentialHelperGetByID(credmgr):
    databaseCredential = credmgr.databaseCredential(1)
    assert getattr(databaseCredential, databaseCredential._nameAttr) == 'test'

def testBotHelperGetByID(credmgr):
    bot = credmgr.bot(1)
    assert getattr(bot, bot._nameAttr) == 'test'

def testBotHelperGetByName(credmgr):
    bot = credmgr.bot('test')
    assert getattr(bot, bot._nameAttr) == 'test'

def testBaseHelperCallWithNameFail(credmgr):
    with pytest.raises(InitializationError):
        _ = credmgr.redditApp('test')