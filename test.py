import random, string
import CredentialManager

genRandomStr = lambda: ''.join([random.choice(string.ascii_letters) for _ in range(6)])


credmgr = CredentialManager.client(host='http://localhost:5000', api_token='L_iqbGj_Aeep3Ws5DH3LOEQPmw8UZ6ek')
# create
redditAppName = f'testRedditApp_{genRandomStr()}'
redditAppClientID = f'testClientID_{genRandomStr}'
redditApp = credmgr.reddit_app.create(redditAppName, client_id=redditAppClientID, app_type='web')
# get
redditApp.createAuthUrl('all', False, 'test')
assert redditApp == credmgr.reddit_app(id=redditApp.id)
# edit
assert redditApp.client_id == redditAppClientID
redditAppNewClientID = f'testClientID_{genRandomStr}'
redditApp.edit(client_id=redditAppNewClientID)
assert redditApp.client_id == redditAppNewClientID
# delete

# bot.edit(reddit_app=1)
# print(bot)
generator = credmgr.bot(owner='spaz')
# items = [i for i in generator]
users = list(credmgr.user())
del bot, credmgr, CredentialManager