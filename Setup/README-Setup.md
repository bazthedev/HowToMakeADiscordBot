# How to Make a Discord Bot:

## Making an Application:
### Go to https://discord.com/developers/applications
### Make a new applications and change anything you want with it
### Go to the Bot page and press make bot user
### Copy the TOKEN and paste into your .env file

## Inviting your bot:
### Now go to the OAuth2 Section and make a link making sure that bot is ticked
### Paste into a new browser window and add to the server of your choice

## Running the bot:
### Now running the code will deploy your bot
### If you see the message in your on_ready function then your bot should be online

## Installing discord.py
### Windows:
#### Press the windows key and type cmd and press enter
#### Type `pip install discord` and run
#### Alternatively if pip is not in your path, type `py -m pip install discord`
#### If python is not installed to your computer, go to https://python.org/ and download a version that suits you

### Linux:
#### Go to your linux terminal
#### Python is usually always installed with linux, if it is not, run `sudo apt install python` in your terminal
#### Run `pip install discord` or `python3 -m pip install discord`
#### If this does not work, try writing `sudo pip install discord` or `sudo python3 pip install discord` - This will prompt for your device password to install discord.py

### Replit:
#### Go to your main.py file and type `import discord`
#### This will auto install for you in your console window
