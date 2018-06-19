import telepot
from telepot.loop import MessageLoop


def BotToken():
    TOKEN = '568848013:AAENwGdsYyesAteYRtRoqHFYuj3cl-0PXZ0'  # get token from command-line

    bot = telepot.Bot(TOKEN)
    return bot
