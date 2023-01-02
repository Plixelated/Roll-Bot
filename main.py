import os
import random
import discord
from discord import app_commands
from dice import dice
from typing import Optional
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")
server = os.getenv("serverID")

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced=False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = server))
            self.synced = True
        print(f'{self.user} has logged in')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(
    name="roll", 
    description="Roll a dice", 
    guild = discord.Object(id = server)
)
@app_commands.describe(
    sides="How many sides?",
    times="How many times?",
    status="Roll with advantage/disadvantage"
)
@app_commands.choices(status=
[
    app_commands.Choice(name="Advantage", value=1),
    app_commands.Choice(name="Disadvantage", value=2),
]
)
async def self(
    interaction: discord.Interaction, 
    sides: int, 
    times: Optional[int], 
    status: Optional[app_commands.Choice[int]]
    ):
    if times != None:
        rollArr = []
        for i in range(times):
            if status.value == 1:
                roll1 = random.randint(1,sides)
                roll2= random.randint(1,sides)
                if roll1 >= roll2:
                    rollArr.append(f'With Advantage: {roll1}')
                else:
                    rollArr.append(f'With Advantage: {roll2}')
            elif status.value == 2:
                roll1 = random.randint(1,sides)
                roll2 = random.randint(1,sides)
                if roll1 <= roll2:
                    rollArr.append(f'With Disadvantage: {roll1}')
                else:
                    rollArr.append(f'With Disadvantage: {roll2}')
            else:
                rollArr.append(random.randint(1,sides))
        
        await interaction.response.send_message(f'You rolled: {rollArr}')
    else:
        if status.value == 1:
            roll1 = random.randint(1,sides)
            roll2= random.randint(1,sides)
            if roll1 >= roll2:
                await interaction.response.send_message(f'You rolled w/ advantage: {roll1}')
            else:
                await interaction.response.send_message(f'You rolled w/ advantage: {roll2}')
        elif status.value == 2:
            roll1 = random.randint(1,sides)
            roll2 = random.randint(1,sides)
            if roll1 <= roll2:
                await interaction.response.send_message(f'You rolled w/ disadvantage: {roll1}')
            else:
                await interaction.response.send_message(f'You rolled w/ disadvantage: {roll2}')
        else:
            await interaction.response.send_message(f'You rolled: {random.randint(1,sides)}')



client.run(token)