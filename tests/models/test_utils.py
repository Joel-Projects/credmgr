from credmgr.models import RedditApp, UserVerification


def testResolveUserWithObject(credentialManager):
    user = credmgr.currentUser
    redditApps = credmgr.redditApps(owner=user)
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)
        assert redditApp.owner == user

def testResolveUserWithUsername(credentialManager):
    user = credmgr.currentUser
    redditApps = credmgr.redditApps(owner=user.username)
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)
        assert redditApp.owner == user

def testResolveModelWithObject(credentialManager):
    redditApp = credmgr.redditApp(26)
    userVerification = credmgr.userVerification.create(userId='testuserid', redditApp=redditApp)
    assert isinstance(userVerification, UserVerification)

def testResolveModelWithId(credentialManager):
    redditApp = credmgr.redditApp(26)
    userVerification = credmgr.userVerification.create(userId='testuserid', redditApp=redditApp.id)
    assert isinstance(userVerification, UserVerification)