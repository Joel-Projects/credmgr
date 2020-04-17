# for _ in range(100):
import CredentialManager
from CredentialManager.models import Bot
from CredentialManager.models.helpers import Paginator


credmgr = CredentialManager.client(host='http://localhost:5000', api_token='L_iqbGj_Aeep3Ws5DH3LOEQPmw8UZ6ek')
# bot = credmgr.bot('test')
#
# bot.edit(reddit_app=1)
# print(bot)
generator = credmgr.bot(owner=2)
# items = [i for i in generator]
users = list(credmgr.user())
del bot, credmgr, CredentialManager