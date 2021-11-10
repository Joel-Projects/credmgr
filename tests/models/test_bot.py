import pytest

from credmgr.exceptions import Conflict, NotFound
from credmgr.models import Bot


def assertCreated(bot, data):
    for key, value in data.items():
        if key in ["redditApp", "sentryToken", "databaseCredential", "owner"]:
            assert getattr(bot, key).id == value
            continue
        assert getattr(bot, key) == value


def testCreateBot(recorder, credentialManager):
    data = {"name": "botName"}
    bot = credentialManager.bot.create(**data)
    assertCreated(bot, data)


def testCreateBotFullParams(recorder, credentialManager):
    data = {
        "name": "botName2",
        "redditApp": 27,
        "sentryToken": 4,
        "databaseCredential": 1,
    }
    bot = credentialManager.bot.create(**data)
    assertCreated(bot, data)


def testCreateBotFullParamsObjects(recorder, credentialManager):
    data = {
        "name": "botName2",
        "redditApp": credentialManager.redditApp(27),
        "sentryToken": credentialManager.sentryToken(4),
        "databaseCredential": credentialManager.databaseCredential(1),
    }
    bot = credentialManager.bot.create(**data)
    for key, value in data.items():
        assert getattr(bot, key) == value


def testCreateBotOtherUser(recorder, credentialManager):
    data = {
        "name": "botName3",
        "redditApp": 29,
        "sentryToken": 12,
        "databaseCredential": 20,
        "owner": 4,
    }
    bot = credentialManager.bot.create(**data)
    assertCreated(bot, data)


def testCreateBotExisting(recorder, credentialManager):
    data = {"name": "botName", "redditApp": 27}
    with pytest.raises(Conflict):
        _ = credentialManager.bot.create(**data)


def testDeleteBot(recorder, credentialManager):
    bot = credentialManager.bot("botName")
    bot.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.bot("botName")


def testEditBot(recorder, credentialManager):
    bot = credentialManager.bot("botName2")
    bot.edit(redditApp=28, name="newBotName")
    assert bot.redditApp.id == 28
    assert bot.name == "newBotName"


def testEditBotWithObject(recorder, credentialManager):
    bot = credentialManager.bot("botName4")
    bot.edit(redditApp=credentialManager.redditApp(28))
    assert bot.redditApp.id == 28


def testEditBotConflictingData(recorder, credentialManager):
    bot = credentialManager.bot("newBotName")
    with pytest.raises(Conflict):
        bot.edit(name="botName4")


def testListBots(recorder, credentialManager):
    bots = credentialManager.bots()
    for bot in bots:
        assert isinstance(bot, Bot)
