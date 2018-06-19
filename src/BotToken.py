import telepot
from telepot.loop import MessageLoop


def BotToken():
    TOKEN = ''  # get token from command-line

    bot = telepot.Bot(TOKEN)
    return bot
