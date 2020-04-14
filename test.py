# for _ in range(100):
import CredentialManager

credmgr = CredentialManager.client(host='http://localhost:5000', api_token='L_iqbGj_Aeep3Ws5DH3LOEQPmw8UZ6ek')
bot = credmgr.bot('test')
bot.edit(reddit_app=1)
print(bot)
del bot, credmgr, CredentialManager