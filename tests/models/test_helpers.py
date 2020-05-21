import pytest
from credmgr.exceptions import InitializationError


def testUserHelperGetByID(credentialManager):
    user = credmgr.user(1)
    assert getattr(user, user._nameAttr) == 'spaz'

def testUserHelperGetByName(credentialManager):
    user = credmgr.user('spaz')
    assert getattr(user, user._nameAttr) == 'spaz'

def testUserVerificationHelperGetByID(credentialManager):
    userVerification = credmgr.userVerification('0123456789')
    assert getattr(userVerification, userVerification._nameAttr) == '0123456789'

def testUserVerificationHelperGetByName(credentialManager):
    data = {'userId': '123456', 'redditAppId': 22}
    userVerification = credmgr.userVerification(**data)
    for key, value in data.items():
        assert getattr(userVerification, key) == value

def testRefreshTokenHelperGetByID(credentialManager):
    refreshToken = credmgr.refreshToken(redditor='Lil_SpazJoekp', redditAppId=2)
    assert getattr(refreshToken, refreshToken._nameAttr) == 'Lil_SpazJoekp'

def testRefreshTokenHelperGetByName(credentialManager):
    data = {'redditor': 'Lil_SpazJoekp', 'redditAppId': 2}
    refreshToken = credmgr.refreshToken(**data)
    for key, value in data.items():
        assert getattr(refreshToken, key) == value

def testRefreshTokenHelperGetByNameFail(credentialManager):
    with pytest.raises(InitializationError):
        _ = credmgr.refreshToken('Lil_SpazJoekp')

def testRefreshTokenHelperGetByNameMissingName(credentialManager):
    data = {'redditAppId': 2}
    with pytest.raises(InitializationError):
        _ = credmgr.refreshToken(**data)

def testSentryTokenHelperGetByID(credentialManager):
    sentryToken = credmgr.sentryToken(1)
    assert getattr(sentryToken, sentryToken._nameAttr) == 'test'

def testRedditAppHelperGetByID(credentialManager):
    redditApp = credmgr.redditApp(1)
    assert getattr(redditApp, redditApp._nameAttr) == 'DankMemesModAbuse'

def testDatabaseCredentialHelperGetByID(credentialManager):
    databaseCredential = credmgr.databaseCredential(1)
    assert getattr(databaseCredential, databaseCredential._nameAttr) == 'test'

def testBotHelperGetByID(credentialManager):
    bot = credmgr.bot(1)
    assert getattr(bot, bot._nameAttr) == 'test'

def testBotHelperGetByName(credentialManager):
    bot = credmgr.bot('test')
    assert getattr(bot, bot._nameAttr) == 'test'

def testBaseHelperCallWithNameFail(credentialManager):
    with pytest.raises(InitializationError):
        _ = credmgr.redditApp('test')