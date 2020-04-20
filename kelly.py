from credmgr import CredentialManager


credmgr = CredentialManager(host='http://localhost:5000', apiToken='L_iqbGj_Aeep3Ws5DH3LOEQPmw8UZ6ek')
bot = credmgr.bot('test_42')
bot2 = credmgr.bot(bot.id)
bot.toDict()
print(bot == bot2)
userVerification = credmgr.userVerification.create('user_id', bot.redditApp)
url = bot.redditApp.genAuthUrl(userVerification=userVerification)
redditor = credmgr.userVerification('user_id').redditor