from credmgr.models import RedditApp, UserVerification


def testResolveUserWithObject(credmgr):
    user = credmgr.currentUser
    redditApps = credmgr.redditApps(owner=user)
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)
        assert redditApp.owner == user

def testResolveUserWithUsername(credmgr):
    user = credmgr.currentUser
    redditApps = credmgr.redditApps(owner=user.username)
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)
        assert redditApp.owner == user

def testResolveModelWithObject(credmgr):
    redditApp = credmgr.redditApp(26)
    userVerification = credmgr.userVerification.create(userId='testuserid', redditApp=redditApp)
    assert isinstance(userVerification, UserVerification)

def testResolveModelWithId(credmgr):
    redditApp = credmgr.redditApp(26)
    userVerification = credmgr.userVerification.create(userId='testuserid', redditApp=redditApp.id)
    assert isinstance(userVerification, UserVerification)