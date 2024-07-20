git clone https://github.com/Plixelated/Roll-Bot.git || (cd Roll-Bot && git checkout docker && git pull origin docker)
cd Roll-Bot

DISCORD_TOKEN=$(cat $DISCORD_TOKEN_FILE)

export DISCORD_TOKEN

python /bot/main.py