# INSTABOT

## Aim
A bot to take part in giveaway posts.
It simulates the action of a normal human account, but at the same time it posts a lot of comments to the wanted posts.

## Human-like actions of the bot
* visiting other websites using google search before visiting instagram
* scrolls up and down at the feed
* likes irrelevant posts from feed
* comments irrelevant posts from feed
* saves irrelevant posts from feed
* opens them without doing anything
* exploring other users' profiles (treats their posts as the feed's ones)
* scrolling up and down on a page slowly, like a human would do
* 1000 comments to choose from randomly
* random time delays between actions

## Advices

### Before activating the bot
* you need to install python, selenium and geckodriver for mozilla firefox
* create four new accounts
* insert the `credentials` at the first lines of the source code of `bot.py`
* the bot keeps a history of the logs in the directory specified by the `history_directory_path` of `line 29`
* specify the `gecko_driver_exe_path` so that the bot can use the gecko driver
* insert the wanted number of comments posted before the termination of the process at the variable `comments_goal` of `line 21`
* if you are not running the bot on windows OS, you might have to modify the `alarm` method of `line 57`

### During bot usage: Slow expansion
* when you start using the bot, at first keep it running for a couple of hours only
* slowly start activating it for more time, so that the time limits of instagram do not detect the unexpected running time of your accounts

## Developer:
* Name: Giannis Athanasiou
* Github: John-Atha
* Email: giannisj3@gmail.com

Note: This bot is still under proccess, there is a danger of your account getting banned in case of excessive usage.