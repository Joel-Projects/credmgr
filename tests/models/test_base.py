def testBaseToDict(credentialManager):
    bot = credentialManager.bot(1)
    exportDict = bot.toDict()
    assert exportDict == {
        'id': 1, 'app_name': 'test', 'owner_id': 1, 'reddit_app': {
            'id': 22,
            'app_name': 'testRedditApp',
            'owner_id': 1,
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'app_description': 'appDescription',
            'user_agent': 'python:testRedditApp by /u/Lil_SpazJoekp',
            'app_type': 'web',
            'redirect_uri': 'https://credmgr.jesassn.org/oauth2/reddit_callback',
            'state': '91893362b02d01c00fb71bc6be02065dedc3356595fc648581ab59a94864a7e4'
        }, 'sentry_token': {
            'id': 4, 'app_name': 'sentryToken', 'owner_id': 1, 'dsn': 'https://key@sentry.jesassn.org/id'
        }, 'database_credential': {
            'id': 1,
            'app_name': 'test',
            'owner_id': 1,
            'database_username': 'postgres',
            'database_host': 'localhost',
            'database': 'postgres',
            'database_flavor': 'postgres',
            'database_port': 5432,
            'database_password': 'postgres',
            'ssh_port': 22
        }
    }

def testBaseEqual(credentialManager):
    bot = credentialManager.bot(1)
    bot2 = credentialManager.bot(1)
    assert bot == bot2

def testBaseNotEqual(credentialManager):
    bot = credentialManager.bot(1)
    bot2 = credentialManager.bot(4)
    assert bot != bot2

def testBaseEqualDifferentType(credentialManager):
    item = credentialManager.bot(1)
    item2 = item.redditApp
    assert item != item2