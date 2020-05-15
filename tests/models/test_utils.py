from credmgr.models import RedditApp


def testResolveUserWithObject(credmgr):
    user = credmgr.currentUser
    redditApps = credmgr.redditApps(owner=user)
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)
        assert redditApp.owner == user

