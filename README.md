# ScrapGradCafe

A telegram bot which scraps information from [GradCafe](https://thegradcafe.com/survey/index.php) site using users input


# Create a bot

<img src="https://core.telegram.org/file/811140763/1/PihKNbjT8UE/03b57814e13713da37" width="20%" height="20%" >

Create a bot using botfather [Botfather](https://telegram.me/botfather)

Creating a new bot
Use the `/newbot` command to create a new bot. The BotFather will ask you for a name and username, then generate an authorization token for your new bot.

The name of your bot is displayed in contact details and elsewhere.

The Username is a short name, to be used in mentions and telegram.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username must end in ‘bot’, e.g. ‘tetris_bot’ or ‘TetrisBot’.

The token is a string along the lines of `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw` that is required to authorize the bot and send requests to the Bot API.

Generating an authorization token
If your existing token is compromised or you lost it for some reason, use the /token command to generate a new one.

Use the token which is generated and place it in the place of the variable `TOKEN = ' '` in [scrapy.py](https://github.com/AsishKakumanu/ScrapGradCafe/blob/6dd5bf81844d7a9b761e4f6233f6b1dc0292c795/src/scrapy.py#L62) file

More bot commands [here](https://core.telegram.org/bots#botfather-commands) 

Now start the bot using the below commands
To start the bot :  ` /start `
To stop the bot : `/stop `


# Query syntax 

`<University_Name>` *Ex : Toronto* <br/>
`<University_Name> <Program_Name>` *Ex:Toronto Applied Computing* <br/>
`<Program_Name>` *Ex: Applied Computing* <br/>


# Screenshots

<div>
  <img src="https://user-images.githubusercontent.com/11143021/40128360-074dc2d8-594f-11e8-9bfa-df143b82c066.png" alt="Screenshot_1" width="30%" height="30%" hspace="10">
  <img src="https://user-images.githubusercontent.com/11143021/40128362-07b483ec-594f-11e8-8ec5-89cda7404163.png" alt="Screenshot_2"
width="30%" height="30%">
  </div>

# Packages used

* Telepot
* regex
* scrapy
* urllib
* beautifulsoup
