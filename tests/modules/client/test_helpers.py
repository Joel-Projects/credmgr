def testUserHelperGetByID(credmgr):
    user = credmgr.user(1)
    assert getattr(user, user._nameAttr) == 'spaz'

def testUserVerificationHelperGetByID(credmgr):
    userVerification = credmgr.userVerification('0123456789')
    assert getattr(userVerification, userVerification._nameAttr) == '0123456789'

def testRefreshTokenHelperGetByID(credmgr):
    refreshToken = credmgr.refreshToken(redditor='Lil_SpazJoekp', redditAppId=2)
    assert getattr(refreshToken, refreshToken._nameAttr) == 'Lil_SpazJoekp'

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