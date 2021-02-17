from credmgr.models import RedditApp, UserVerification


def testResolveUserWithObject(credentialManager):
    user = credentialManager.currentUser
    redditApps = credentialManager.redditApps(owner=user)
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)
        assert redditApp.owner == user


def testResolveUserWithUsername(credentialManager):
    user = credentialManager.currentUser
    redditApps = credentialManager.redditApps(owner=user.username)
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)
        assert redditApp.owner == user


def testResolveModelWithObject(credentialManager):
    redditApp = credentialManager.redditApp(26)
    userVerification = credentialManager.userVerification.create(
        userId="testuserid", redditApp=redditApp
    )
    assert isinstance(userVerification, UserVerification)


def testResolveModelWithId(credentialManager):
    redditApp = credentialManager.redditApp(26)
    userVerification = credentialManager.userVerification.create(
        userId="testuserid", redditApp=redditApp.id
    )
    assert isinstance(userVerification, UserVerification)
