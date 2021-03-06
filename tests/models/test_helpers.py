import pytest

from credmgr.exceptions import InitializationError


def testUserHelperGetByID(recorder, credentialManager):
    user = credentialManager.user(1)
    assert getattr(user, user._nameAttr) == "spaz"


def testUserHelperGetByName(recorder, credentialManager):
    user = credentialManager.user("spaz")
    assert getattr(user, user._nameAttr) == "spaz"


def testUserVerificationHelperGetByID(recorder, credentialManager):
    userVerification = credentialManager.userVerification("0123456789")
    assert getattr(userVerification, userVerification._nameAttr) == "0123456789"


def testUserVerificationHelperGetByName(recorder, credentialManager):
    data = {"userId": "123456", "redditAppId": 22}
    userVerification = credentialManager.userVerification(**data)
    for key, value in data.items():
        assert getattr(userVerification, key) == value


def testRefreshTokenHelperGetByID(recorder, credentialManager):
    refreshToken = credentialManager.refreshToken(
        redditor="Lil_SpazJoekp", redditAppId=2
    )
    assert getattr(refreshToken, refreshToken._nameAttr) == "Lil_SpazJoekp"


def testRefreshTokenHelperGetByName(recorder, credentialManager):
    data = {"redditor": "Lil_SpazJoekp", "redditAppId": 2}
    refreshToken = credentialManager.refreshToken(**data)
    for key, value in data.items():
        assert getattr(refreshToken, key) == value


def testRefreshTokenHelperGetByNameFail(recorder, credentialManager):
    with pytest.raises(InitializationError):
        _ = credentialManager.refreshToken("Lil_SpazJoekp")


def testRefreshTokenHelperGetByNameMissingName(recorder, credentialManager):
    data = {"redditAppId": 2}
    with pytest.raises(InitializationError):
        _ = credentialManager.refreshToken(**data)


def testSentryTokenHelperGetByID(recorder, credentialManager):
    sentryToken = credentialManager.sentryToken(1)
    assert getattr(sentryToken, sentryToken._nameAttr) == "test"


def testRedditAppHelperGetByID(recorder, credentialManager):
    redditApp = credentialManager.redditApp(1)
    assert getattr(redditApp, redditApp._nameAttr) == "DankMemesModAbuse"


def testDatabaseCredentialHelperGetByID(recorder, credentialManager):
    databaseCredential = credentialManager.databaseCredential(1)
    assert getattr(databaseCredential, databaseCredential._nameAttr) == "test"


def testBotHelperGetByID(recorder, credentialManager):
    bot = credentialManager.bot(1)
    assert getattr(bot, bot._nameAttr) == "test"


def testBotHelperGetByName(recorder, credentialManager):
    bot = credentialManager.bot("test")
    assert getattr(bot, bot._nameAttr) == "test"


def testBaseHelperCallWithNameFail(recorder, credentialManager):
    with pytest.raises(InitializationError):
        _ = credentialManager.redditApp("test")
