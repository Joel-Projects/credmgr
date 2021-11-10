import time
from functools import partial

import asyncpraw
import mock
import praw
import pytest

from credmgr.exceptions import Conflict, InitializationError, NotFound, ServerError
from credmgr.models import RedditApp


def testCreateRedditApp(recorder, credentialManager):
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


def testCreateRedditAppOtherUser(recorder, credentialManager):
    data = {"name": "testRedditApp", "clientId": "clientId", "owner": 4}
    redditApp = credentialManager.redditApp.create(**data)
    for key, value in data.items():
        if key == "owner":
            assert getattr(redditApp, key).id == value
            continue
        assert getattr(redditApp, key) == value


def testCreateRedditAppBadParams(recorder, credentialManager):
    data = {"name": "te", "clientId": "clientId2"}
    with pytest.raises(ServerError):
        _ = credentialManager.redditApp.create(**data)


def testCreateRedditAppExisting(recorder, credentialManager):
    data = {"name": "redditApp", "clientId": "clientId"}
    with pytest.raises(Conflict):
        _ = credentialManager.redditApp.create(**data)


def testDeleteRedditApp(recorder, credentialManager):
    redditApp = credentialManager.redditApp(3)
    redditApp.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.redditApp(3)


def testEditRedditApp(recorder, credentialManager):
    redditApp = credentialManager.redditApp(6)
    redditApp.edit(clientId="newClientId")
    assert redditApp.clientId == "newClientId"


def testEditRedditAppConflictingData(recorder, credentialManager):
    redditApp = credentialManager.redditApp(6)
    with pytest.raises(Conflict):
        redditApp.edit(clientId="clientId")


def testListRedditApps(recorder, credentialManager):
    redditApps = credentialManager.redditApps()
    for redditApp in redditApps:
        assert isinstance(redditApp, RedditApp)


def testListRedditAppsWithRedditApp(recorder, credentialManager):
    with pytest.raises(InitializationError):
        _ = credentialManager.redditApp()


def testCreateRedditAppWithoutUserAgent(recorder, credentialManager):
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


class CustomSyncReddit(praw.Reddit):
    pass


class CustomAsyncReddit(asyncpraw.Reddit):
    pass


@pytest.mark.parametrize("use_async", [True, False], ids=["use_async", "not_use_async"])
@pytest.mark.parametrize("use_cache", [True, False], ids=["use_cache", "not_use_cache"])
@pytest.mark.parametrize(
    "use_custom_reddit_class",
    [True, False],
    ids=["custom_reddit_class", "no_custom_class"],
)
def testRedditAppReddit(
    recorder, credentialManager, use_async, use_cache, use_custom_reddit_class
):
    redditApp = credentialManager.redditApp(2)
    reddit_class = None
    if use_custom_reddit_class:
        reddit_class = CustomAsyncReddit if use_async else CustomSyncReddit
    reddit = redditApp.reddit(use_async=use_async, reddit_class=reddit_class)
    same = reddit is redditApp.reddit(
        use_async=use_async, use_cache=use_cache, reddit_class=reddit_class
    )
    assert (
        type(reddit) == (CustomAsyncReddit if use_async else CustomSyncReddit)
        if reddit_class
        else (asyncpraw.Reddit if use_async else praw.Reddit)
    )
    assert same == use_cache
    assert isinstance(reddit, praw.Reddit if not use_async else asyncpraw.Reddit)


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


def testRedditAppRedditWithRedditor(recorder, credentialManager):
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


def testRedditAppRedditWithBadRedditor(recorder, credentialManager):
    redditApp = credentialManager.redditApp(2)
    with pytest.raises(NotFound):
        _ = redditApp.reddit("BadRedditor")


def testRedditAppGenAuthUrlVerificationScopes(recorder, credentialManager):
    redditApp = credentialManager.redditApp(19)
    url = redditApp.genAuthUrl(scopes="read")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=read+identity&state=91893362b02d01c00fb71bc6be02065dedc3356595fc648581ab59a94864a7e4"
    )


def testRedditAppGenAuthUrlVerificationAllScopes(recorder, credentialManager):
    redditApp = credentialManager.redditApp(19)
    url = redditApp.genAuthUrl(scopes="all")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=%2A&state=91893362b02d01c00fb71bc6be02065dedc3356595fc648581ab59a94864a7e4"
    )


def testRedditAppGenAuthUrlVerification(recorder, credentialManager):
    redditApp = credentialManager.redditApp(6)
    url = redditApp.genAuthUrl()
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=7ce31a95e1abc2a41673406ff87da51932acf1047cbf2eec1beb1f783d81cfd4"
    )


def testRedditAppGenAuthUrlAuthencation(recorder, credentialManager):
    redditApp = credentialManager.redditApp(6)
    url = redditApp.genAuthUrl(permanent=True)
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=permanent&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=7ce31a95e1abc2a41673406ff87da51932acf1047cbf2eec1beb1f783d81cfd4"
    )


def testRedditAppGenAuthUrlUserVerification(recorder, credentialManager):
    redditApp = credentialManager.redditApp(6)
    url = redditApp.genAuthUrl(userVerification=22)
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=newClientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=N2NlMzFhOTVlMWFiYzJhNDE2NzM0MDZmZjg3ZGE1MTkzMmFjZjEwNDdjYmYyZWVjMWJlYjFmNzgzZDgxY2ZkNDoyMg%3D%3D"
    )


def testRedditAppGenAuthUrlUserVerificationCreate(recorder, credentialManager):
    redditApp = credentialManager.redditApp(19)
    url = redditApp.genAuthUrl(userVerification="newId")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=OTE4OTMzNjJiMDJkMDFjMDBmYjcxYmM2YmUwMjA2NWRlZGMzMzU2NTk1ZmM2NDg1ODFhYjU5YTk0ODY0YTdlNDo8VXNlclZlcmlmaWNhdGlvbiBpZD0yMywgdXNlcklkPSduZXdJZCc-"
    )


def testRedditAppGenAuthUrlUserVerificationCreateExisting(recorder, credentialManager):
    redditApp = credentialManager.redditApp(22)
    url = redditApp.genAuthUrl(userVerification="newId")
    assert (
        url
        == "https://www.reddit.com/api/v1/authorize?client_id=clientId&duration=temporary&redirect_uri=https%3A%2F%2Fcredmgr.jesassn.org%2Foauth2%2Freddit_callback&response_type=code&scope=identity&state=OTE4OTMzNjJiMDJkMDFjMDBmYjcxYmM2YmUwMjA2NWRlZGMzMzU2NTk1ZmM2NDg1ODFhYjU5YTk0ODY0YTdlNDpuZXdJZA%3D%3D"
    )
