import pytest

from credmgr.exceptions import Conflict, InitializationError, NotFound
from credmgr.models import Bot



def assertCreated(bot, data):
    for key, value in data.items():
        if key in ['redditApp', 'sentryToken', 'databaseCredential', 'owner']:
            assert getattr(bot, key).id == value
            continue
        assert getattr(bot, key) == value

def testCreateBot(credmgr):
    data = {'name': 'botName'}
    bot = credmgr.bot.create(**data)
    assertCreated(bot, data)

def testCreateBotFullParams(credmgr):
    data = {'name': 'botName2', 'redditApp': 27, 'sentryToken': 4, 'databaseCredential': 1}
    bot = credmgr.bot.create(**data)
    assertCreated(bot, data)

def testCreateBotFullParamsObjects(credmgr):
    data = {'name': 'botName2', 'redditApp': credmgr.redditApp(27), 'sentryToken': credmgr.sentryToken(4), 'databaseCredential': credmgr.databaseCredential(1)}
    bot = credmgr.bot.create(**data)
    for key, value in data.items():
        assert getattr(bot, key) == value

def testCreateBotOtherUser(credmgr):
    data = {'name': 'botName3', 'redditApp': 29, 'sentryToken': 12, 'databaseCredential': 20, 'owner': 4}
    bot = credmgr.bot.create(**data)
    assertCreated(bot, data)

def testCreateBotExisting(credmgr):
    data = {'name': 'botName', 'redditApp': 27}
    with pytest.raises(Conflict):
        _ = credmgr.bot.create(**data)

def testDeleteBot(credmgr):
    bot = credmgr.bot('botName')
    bot.delete()
    with pytest.raises(NotFound):
        _ = credmgr.bot('botName')

def testEditBot(credmgr):
    bot = credmgr.bot('botName2')
    bot.edit(redditApp=28, name='newBotName')
    assert bot.redditApp.id == 28
    assert bot.name == 'newBotName'

def testEditBotConflictingData(credmgr):
    bot = credmgr.bot('newBotName')
    with pytest.raises(Conflict):
        bot.edit(name='botName4')

def testListBots(credmgr):
    bots = credmgr.bots()
    for bot in bots:
        assert isinstance(bot, Bot)