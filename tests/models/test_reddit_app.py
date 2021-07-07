import time
from functools import partial

import mock
import praw
import pytest
from credmgr.models import RedditApp

from credmgr.exceptions import Conflict, InitializationError, NotFound, ServerError


def testCreateRedditApp(credentialManager):
    data = {
        "name": "testRedditApp",
        "clientId": "clientId",
        "clientSecret": "clientSecret",
        "userAgent": "userAgent",
        "appDescription": "appDescription",
    }
    redditApp = credentialManager.redditApp.create(**data)
    for key, value in data.items():
        assert getattr(redditApp, key) == value


def testCreateRedditAppOtherUser(credentialManager):
    data = {"name": "testRedditApp", "clientId": "clientId", "owner": 4}
    redditApp = credentialManager.redditApp.create(**data)
    for key, value in data.items():
        if key == "owner":
            assert getattr(redditApp, key).id == value
            continue
        assert getattr(redditApp, key) == value


def testCreateRedditAppBadParams(credentialManager):
    data = {"name": "te", "clientId": "clientId2"}
    with pytest.raises(ServerError):
        _ = credentialManager.redditApp.create(**data)


def testCreateRedditAppExisting(credentialManager):
    data = {"name": "redditApp", "clientId": "clientId"}
    with pytest.raises(Conflict):
        _ = credentialManager.redditApp.create(**data)


def testDeleteRedditApp(credentialManager):
    redditApp = credentialManager.redditApp(3)
    redditApp.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.redditApp(3)


def testEditRedditApp(credentialManager):
    redditApp = credentialManager.redditApp(6)
    redditApp.edit(clientId="newClientId")
    assert redditApp.clientId == "newClientId"


def testEditRedditAppConflictingData(credentialManager):
    redditApp = credentialManager.redditApp(6)
    with pytest.raises(Conflict):
        redditApp.edit(clientId="clientId")


def testListRedditApps(credentialManager):
    redditApps = credentialManager.redditApps()
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)


def testListRedditAppsWithRedditApp(credentialManager):
    with pytest.raises(InitializationError):
        _ = credentialManager.redditApp()


def testCreateRedditAppWithoutUserAgent(credentialManager):
    data = {
        "name": "testRedditApp",
        "clientId": "clientId",
        "clientSecret": "clientSecret",
        "appDescription": "appDescription",
    }
    redditApp = credentialManager.redditApp.create(**data)
    assert redditApp.userAgent == "python:testRedditApp by /u/Lil_SpazJoekp"
    for key, value in data.items():
        assert getattr(redditApp, key) == value


def testRedditAppReddit(credentialManager):
    redditApp = credentialManager.redditApp(2)
    reddit = redditApp.reddit()
    assert isinstance(reddit, praw.Reddit)


def patched__request_token(self, **data):
    payload = {
        "access_token": "access_token",
        "token_type": "bearer",
        "expires_in": 3600,
        "refresh_token": "new_token",
        "scope": "account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modmail modothers modposts modself modtraffic modwiki mysubreddits privatemessages read report save structuredstyles submit subscribe vote wikiedit wikiread",
    }
    pre_request_time = time.time()
    self._expiration_timestamp = pre_request_time - 10 + payload["expires_in"]
    self.access_token = payload["access_token"]
    if "refresh_token" in payload:
        self.refresh_token = payload["refresh_token"]
    self.scopes = set(payload["scope"].split(" "))


def testRedditAppRedditWithRedditor(credentialManager):
    redditApp = credentialManager.redditApp(2)
    reddit = redditApp.reddit("Lil_SpazJoekp")
    assert isinstance(reddit, praw.Reddit)
    assert not reddit.read_only
    response = mock.Mock(status_code=200)
    response.json.return_value = {"name": "Lil_SpazJoekp"}
    with mock.patch(
        "prawcore.requestor.Requestor.request", return_value=response, create=True
    ):
        with mock.patch("prawcore.rate_limit.RateLimiter.delay"):
            with mock.patch("prawcore.rate_limit.RateLimiter.update"):
                reddit._core._authorizer._request_token = partial(
                    patched__request_token, self=reddit._core._authorizer
                )
                reddit._core._authorizer.refresh()
                assert reddit.user.me() == "Lil_SpazJoekp"


def testRedditAppRedditWithBadRedditor(credentialManager):
    redditApp = credentialManager.redditApp(2)
    with pytest.raises(NotFound):
        _ = redditApp.reddit("BadRedditor")


def testRedditAppGenAuthUrlVerificationScopes(credentialManager):
    redditApp = credentialManager.redditApp(19)
    url = redditApp.genAuthUrl(scopes="read")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=read+identity&state=91893362b02d01c00fb71bc6be02065dedc3356595fc648581ab59a94864a7e4"
    )


def testRedditAppGenAuthUrlVerificationAllScopes(credentialManager):
    redditApp = credentialManager.redditApp(19)
    url = redditApp.genAuthUrl(scopes="all")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=%2A&state=91893362b02d01c00fb71bc6be02065dedc3356595fc648581ab59a94864a7e4"
    )


def testRedditAppGenAuthUrlVerification(credentialManager):
    redditApp = credentialManager.redditApp(6)
    url = redditApp.genAuthUrl()
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=7ce31a95e1abc2a41673406ff87da51932acf1047cbf2eec1beb1f783d81cfd4"
    )


def testRedditAppGenAuthUrlAuthencation(credentialManager):
    redditApp = credentialManager.redditApp(6)
    url = redditApp.genAuthUrl(permanent=True)
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=permanent&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=7ce31a95e1abc2a41673406ff87da51932acf1047cbf2eec1beb1f783d81cfd4"
    )


def testRedditAppGenAuthUrlUserVerification(credentialManager):
    redditApp = credentialManager.redditApp(6)
    url = redditApp.genAuthUrl(userVerification=22)
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=N2NlMzFhOTVlMWFiYzJhNDE2NzM0MDZmZjg3ZGE1MTkzMmFjZjEwNDdjYmYyZWVjMWJlYjFmNzgzZDgxY2ZkNDoyMg%3D%3D"
    )


def testRedditAppGenAuthUrlUserVerificationCreate(credentialManager):
    redditApp = credentialManager.redditApp(19)
    url = redditApp.genAuthUrl(userVerification="newId")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=OTE4OTMzNjJiMDJkMDFjMDBmYjcxYmM2YmUwMjA2NWRlZGMzMzU2NTk1ZmM2NDg1ODFhYjU5YTk0ODY0YTdlNDo8VXNlclZlcmlmaWNhdGlvbiBpZD0yMywgdXNlcklkPSduZXdJZCc-"
    )


def testRedditAppGenAuthUrlUserVerificationCreateExisting(credentialManager):
    redditApp = credentialManager.redditApp(22)
    url = redditApp.genAuthUrl(userVerification="newId")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=OTE4OTMzNjJiMDJkMDFjMDBmYjcxYmM2YmUwMjA2NWRlZGMzMzU2NTk1ZmM2NDg1ODFhYjU5YTk0ODY0YTdlNDpuZXdJZA%3D%3D"
    )
