# MessageCountingBot
This bot will count the amount of messages from each participant in a group chat.

It will send rude messages to the least participated users and some good words to the most participated ones. 

Here are some simple steps to run this bot:
    1. Install the latest Python version. I am using Python 3.10 with this project so this one will definitely work.
    2. Run "python3 -m venv venv" inside root folder of this project to create a virtual environment.
    3. Run "source venv/scripts/activate" in git bash if you're on windows or "source venv/bin/activate" if you're on MacOS or Linux to activate your new environment.
    4. Run "pip install -r reqs.txt" to install all of the required libraries in your environment.
    5. Type in your bot token in .token file. Your token should go after '='.
    6. Run bot.py via bash with "python bot.py".

You can change this bot's messages in 'dic/dictionary.py' or check its logs in __pycache__ and 'logs/log.txt'

!!There is a little chance that i forgon to change the env file name in 'config_reader.py'. Please check. There should be "env_file = '.token'".
