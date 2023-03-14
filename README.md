# Telegram Group Chat Message Counter Bot

This bot will count the amount of messages from each participant in a group chat.

It will send rude messages to the least participated users and some good words to the most participated ones.

## Usage

1. Install the latest Python version. I am using Python 3.10 with this project so this one will definitely work.
2. Run `python3 -m venv venv` inside root folder of this project to create a virtual environment.
3. Run `source venv/scripts/activate` in git bash if you're on windows or `source venv/bin/activate` if you're on MacOS or Linux to activate your new environment.
4. Run `pip install -r reqs.txt` to install all of the required libraries in your environment.
5. Type in your bot token in `.token` file. Your token should go after `=`. 
6. Run `bot.py` via bash with `python bot.py`.

## Customization

You can change this bot's messages in `dic/dictionary.py` or check its logs in `pycache` and `logs/log.txt`

## Notes

**Note 1:** There is a little chance that I forgot to change the env file name in `config_reader.py`. Please check. There should be `env_file = '.token'`.

**Note 2:** This bot is still under development so there are definitely a lot of bugs and mistakes. 

**Note 3:** You can contact me in telegram via `t.me/smbrinee` to talk about quick-fixes and add-ons for this bot. 

