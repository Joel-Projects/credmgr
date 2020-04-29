import praw
import pytest
from credmgr.exceptions import Conflict, NotFound, ServerError


def testCreateRedditApp(credmgr):
    data = {'appName': 'testRedditApp', 'clientId': 'clientId', 'clientSecret': 'clientSecret', 'userAgent': 'userAgent'}
    redditApp = credmgr.redditApp.create(**data)
    for key, value in data.items():
        assert getattr(redditApp, key) == value

def testCreateRedditAppBadParams(credmgr):
    data = {'appName': 'te', 'clientId': 'clientId2'}
    with pytest.raises(ServerError):
        _ = credmgr.redditApp.create(**data)

def testCreateRedditAppExisting(credmgr):
    data = {'appName': 'redditApp', 'clientId': 'clientId'}
    with pytest.raises(Conflict):
        _ = credmgr.redditApp.create(**data)

def testDeleteRedditApp(credmgr):
    redditApp = credmgr.redditApp(3)
    redditApp.delete()
    with pytest.raises(NotFound):
        _ = credmgr.redditApp(3)

def testEditRedditApp(credmgr):
    redditApp = credmgr.redditApp(6)
    redditApp.edit(clientId='newClientId')
    assert redditApp.clientId == 'newClientId'

def testEditRedditAppConflictingData(credmgr):
    redditApp = credmgr.redditApp(6)
    with pytest.raises(Conflict):
        redditApp.edit(clientId='clientId')

def testRedditAppReddit(credmgr):
    redditApp = credmgr.redditApp(2)
    reddit = redditApp.reddit()
    assert isinstance(reddit, praw.Reddit)

def testRedditAppRedditWithRedditor(credmgr, recorder):
    redditApp = credmgr.redditApp(2)
    reddit = redditApp.reddit('Lil_SpazJoekp')
    assert isinstance(reddit, praw.Reddit)
    assert reddit.config.refresh_token is not None

def testRedditAppRedditWithBadRedditor(credmgr):
    redditApp = credmgr.redditApp(2)
    with pytest.raises(NotFound):
        _ = redditApp.reddit('BadRedditor')

def testRedditAppGenAuthUrlVerification(credmgr):
    redditApp = credmgr.redditApp(6)
    url = redditApp.genAuthUrl()
    assert url == 'https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=7ce31a95e1abc2a41673406ff87da51932acf1047cbf2eec1beb1f783d81cfd4'

def testRedditAppGenAuthUrlAuthencation(credmgr):
    redditApp = credmgr.redditApp(6)
    url = redditApp.genAuthUrl(permanent=True)
    assert url == 'https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=permanent&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=7ce31a95e1abc2a41673406ff87da51932acf1047cbf2eec1beb1f783d81cfd4'

def testRedditAppGenAuthUrlUserVerification(credmgr):
    redditApp = credmgr.redditApp(6)
    url = redditApp.genAuthUrl(userVerification=22)
    assert url == 'https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=N2NlMzFhOTVlMWFiYzJhNDE2NzM0MDZmZjg3ZGE1MTkzMmFjZjEwNDdjYmYyZWVjMWJlYjFmNzgzZDgxY2ZkNDoyMg%3D%3D'

def testRedditAppGenAuthUrlUserVerificationCreate(credmgr):
    redditApp = credmgr.redditApp(6)
    url = redditApp.genAuthUrl(userVerification='newId')
    assert url == 'https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=7ce31a95e1abc2a41673406ff87da51932acf1047cbf2eec1beb1f783d81cfd4'

def testListRedditApps(credmgr):
    redditApps = credmgr.redditApps()
    redditApps = [i for i in redditApps]
    assert isinstance(redditApps, list)