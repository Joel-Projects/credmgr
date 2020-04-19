import random, string
from credmgr import CredentialManager

genRandomStr = lambda: ''.join([random.choice(string.ascii_letters) for _ in range(6)])
credmgr = CredentialManager(host='http://localhost:5000', apiToken='L_iqbGj_Aeep3Ws5DH3LOEQPmw8UZ6ek')
# create
redditAppName = f'testRedditApp_{genRandomStr()}'
redditAppClientID = f'testClientID_{genRandomStr}'
redditApp = credmgr.redditApp.create(redditAppName, clientId=redditAppClientID, appType='web')
# get
# redditApp.createAuthUrl('all', False, 'test')
redditApp = credmgr.redditApp(2)
bot = credmgr.bot('test_42')
bot.edit(redditApp=redditApp)
userVerification = credmgr.userVerification.create('testid', redditApp)
repr(userVerification)
authUrl = redditApp.genAuthUrl(userVerification=userVerification)
assert redditApp == credmgr.redditApp(id=redditApp.id)
# edit
assert redditApp.clientId == redditAppClientID
redditAppNewClientID = f'testClientID_{genRandomStr}'
redditApp.edit(clientId=redditAppNewClientID)
assert redditApp.clientId == redditAppNewClientID
# delete

# bot.edit(redditApp=1)
# print(bot)
generator = credmgr.bot(owner='spaz')
# items = [i for i in generator]
users = list(credmgr.user())
del bot, credmgr, CredentialManager