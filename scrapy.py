import regex as re  # learn more: https://python.org/pypi/regex
import scrapy
import urllib.request, urllib.error, urllib.parse
import pandas as pd
from bs4 import BeautifulSoup

import sys
import time
import telepot
from telepot.loop import MessageLoop

status_key = {'A': 'American Student', 'U': 'International Student, with US degree',
              'I': 'International Student, without US degree', 'O': 'Other', None: 'Unknown'}
String_list = list()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        keystr = str(msg['text'])
        print(keystr)
        gradcafe = 'https://thegradcafe.com/survey/index.php?q={}&t=a&o=&pp=50'.format(keystr)
        req = urllib.request.Request(gradcafe, headers={'User-Agent': "Chrome Browser"})
        con = urllib.request.urlopen(req)
        soup = BeautifulSoup(con, "html.parser")
        right_table = soup.find('table', class_="results narrow-table")

        # bot.sendMessage(chat_id, KEYWORDS)

        for row in right_table.findAll("tr"):
            cells = row.findAll("td")

            Undergrad_GPA = ''
            GRE = ''
            institution = cells[0].find(text=True)
            ins = re.sub('[^A-Za-z0-9 ]+', '', institution)
            Program = cells[1].find(text=True)
            Decision = cells[2].find(text=True)
            Scores = cells[2].findAll(text=True)
            length = len(Scores)

            if length > 8:
                Undergrad_GPA = Scores[3]
                GRE = Scores[5]
            Status = cells[3].find(text=True)
            Date_Added = cells[4].find(text=True)
            Notes = cells[5].find(text=True)

            FormedString = str("Institution : " + str(ins) + "\n" + "Program : " + str(Program) + "\n" + "Decision : " + str(Decision) + "\n" + "Undergrad_GPA " + str(Undergrad_GPA) + "\n" + "GRE(V/Q/W) " + str(
                GRE) + "\n" + "Status : " + str(status_key.get(Status)) + "\n" + "Date_Added : " + str(
                Date_Added) + "\n" + "Notes : " + str(Notes) + "\n\n")

            String_list.append(FormedString)

        for i in range(1, len(String_list)):
            print((String_list[i]))
            print("")
            bot.sendMessage(chat_id,String_list[i])


TOKEN = ''  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)



if __name__ == '__main__':
    MessageLoop()