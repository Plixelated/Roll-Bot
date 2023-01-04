import os
import discord
from discord import app_commands
from typing import Optional
from dotenv import load_dotenv
from dice import dice

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
    die = dice(sides)

    if times != None:
        if status:
            if status.value == 1:
                rolls = die.roll_multi_adv(times)
                await interaction.response.send_message(f'With Advantage You rolled: {rolls}')
            elif status.value == 2:
                rolls = die.roll_multi_dis(times)
                await interaction.response.send_message(f'With Disadvantage You rolled: {rolls}')
        else:
            rolls = die.roll_multi(times)
            await interaction.response.send_message(f'You rolled: {rolls}')
    else:
        if status:
            if status.value == 1:
                roll = die.roll_adv()
                await interaction.response.send_message(f'With Advantage You rolled: {roll}')
            elif status.value == 2:
                roll = die.roll_dis()
                await interaction.response.send_message(f'With Disadvantage You rolled: {roll}')
        else:
            roll = die.roll()
            await interaction.response.send_message(f'You rolled: {roll}')

        



client.run(token)