from credmgr import CredentialManager

credentialManager = CredentialManager()

bot = credentialManager.bot("botName")
reddit = bot.redditApp.reddit("authorizedRedditor")

subreddit = reddit.subreddit("dankmemes")
stream = subreddit.stream.comments()

while True:
    for comment in stream:
        if "mods gay" in comment.body and not comment.saved:
            comment.reply("no u")
            comment.save()
