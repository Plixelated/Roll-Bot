#!/bin/bash

if [ ! -d "Roll-Bot" ]; then
    git clone https://github.com/Plixelated/Roll-Bot.git 
fi

cd Roll-Bot

git checkout docker 
git pull origin docker

if [ ! -f "$DISCORD_TOKEN_FILE" ]; then
    echo "Token file not found: $DISCORD_TOKEN_FILE"
    exit 1
fi

DISCORD_TOKEN=$(cat $DISCORD_TOKEN_FILE)

export DISCORD_TOKEN

python /app/Roll-Bot/bot/main.py