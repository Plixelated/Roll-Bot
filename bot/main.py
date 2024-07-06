import os
import discord
from discord import app_commands
from typing import Optional
from dotenv import load_dotenv
from dice import dice as d

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
#server = os.getenv("serverID")

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced=False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user} has logged in')

client = aclient()
tree = app_commands.CommandTree(client)

#ROLL DIE
@tree.command(
    name="roll", 
    description="Roll a dice", 
)
@app_commands.describe(
    dice="Which Dice Would You Like To Roll?",
    mod="Are There Any Modifiers To Your Dice?",
    number="How Many Dice Do You Want To Roll?",
    status="Are You Rolling with Advantage or Disadvantage?"
)
@app_commands.choices(dice=
[
    app_commands.Choice(name="D20",value=20),
    app_commands.Choice(name="D12",value=12),
    app_commands.Choice(name="D10",value=10),
    app_commands.Choice(name="D8",value=8),
    app_commands.Choice(name="D6",value=6),
    app_commands.Choice(name="D4",value=4),
    app_commands.Choice(name="D100",value=100)
]
)
@app_commands.choices(status=
[
    app_commands.Choice(name="Advantage", value=1),
    app_commands.Choice(name="Disadvantage", value=2),
]
)
async def roll(
    interaction: discord.Interaction, 
    dice: app_commands.Choice[int],
    mod:Optional[int],
    number: Optional[int], 
    status: Optional[app_commands.Choice[int]]
    ):

    new_die = d(dice.value)

    if number != None:
        if status:
            if status.value == 1:
                rolls = new_die.roll_multi_adv(number)
                total = new_die.get_multi_adv_total(rolls) + mod if mod != None else new_die.get_multi_adv_total(rolls)
                status_text = "*(Advantage)*"
            elif status.value == 2:
                rolls = new_die.roll_multi_dis(number)
                total = new_die.get_multi_dis_total(rolls) + mod if mod != None else new_die.get_multi_dis_total(rolls)
                status_text = "*(Disadvantage)*"
        else:
            rolls = new_die.roll_multi(number)
            total = sum(rolls) + mod if mod != None else sum(rolls)
            status_text = ""
        
        msg = f'Rolls {status_text}: {rolls}\nModifier: {mod}\nTotal: **{total}**' if mod != None else f'Rolls {status_text}: {rolls}\nTotal: **{total}**'
        await interaction.response.send_message(msg)
    else:
        if status:
            if status.value == 1:
                roll = new_die.roll_adv()
                total = max(roll) + mod if mod != None else max(roll)
                status_text = "*(Advantage)*"
            elif status.value == 2:
                roll = new_die.roll_dis()
                total = min(roll) + mod if mod != None else min(roll)
                status_text = "*(Disadvantage)*"
            
            msg = f'Rolls {status_text}: {roll}\nModifier: {mod}\nTotal: **{total}**' if mod != None else f'Rolls {status_text}: {roll}\nTotal: **{total}**'
        else:
            roll = new_die.roll()
            total = roll + mod if mod != None else roll
            msg = f'Roll: {roll}\nModifier:{mod}\nTotal: **{total}**' if mod != None else f'Roll: **{roll}**'
            
        await interaction.response.send_message(msg)

#CUSTOM DICE
@tree.command(
    name="custom", 
    description="Roll a custom dice", 
)
@app_commands.describe(
    sides="What Kind of Dice Would You Like to Roll?",
    mod="Are There Any Modifiers To Your Dice?",
    number="How Many Dice Do You Want To Roll?",
    status="Are You Rolling with Advantage or Disadvantage?"
)
@app_commands.choices(status=
[
    app_commands.Choice(name="Advantage", value=1),
    app_commands.Choice(name="Disadvantage", value=2),
]
)
async def custom(
    interaction: discord.Interaction, 
    sides: int,
    mod:Optional[int],
    number: Optional[int], 
    status: Optional[app_commands.Choice[int]]
    ):
    
    new_die = d(sides)

    if number != None:
        if status:
            if status.value == 1:
                rolls = new_die.roll_multi_adv(number)
                total = new_die.get_multi_adv_total(rolls) + mod if mod != None else new_die.get_multi_adv_total(rolls)
                status_text = "*(Advantage)*"
            elif status.value == 2:
                rolls = new_die.roll_multi_dis(number)
                total = new_die.get_multi_dis_total(rolls) + mod if mod != None else new_die.get_multi_dis_total(rolls)
                status_text = "*(Disadvantage)*"
        else:
            rolls = new_die.roll_multi(number)
            total = sum(rolls) + mod if mod != None else sum(rolls)
            status_text = ""
        
        msg = f'Rolls {status_text}: {rolls}\nModifier: {mod}\nTotal: **{total}**' if mod != None else f'Rolls {status_text}: {rolls}\nTotal: **{total}**'
        await interaction.response.send_message(msg)
    else:
        if status:
            if status.value == 1:
                roll = new_die.roll_adv()
                total = max(roll) + mod if mod != None else max(roll)
                status_text = "*(Advantage)*"
            elif status.value == 2:
                roll = new_die.roll_dis()
                total = min(roll) + mod if mod != None else min(roll)
                status_text = "*(Disadvantage)*"
            
            msg = f'Rolls {status_text}: {roll}\nModifier: {mod}\nTotal: **{total}**' if mod != None else f'Rolls {status_text}: {roll}\nTotal: **{total}**'
        else:
            roll = new_die.roll()
            total = roll + mod if mod != None else roll
            msg = f'Roll: {roll}\nModifier:{mod}\nTotal: **{total}**' if mod != None else f'Roll: **{roll}**'
            
        await interaction.response.send_message(msg)

#QUICK ROLL
@tree.command(
    name="quickroll", 
    description="Quickly roll a die", 
)
@app_commands.describe(
    sides="What Kind of Dice Would You Like to Roll?",
    mod="Are There Any Modifiers To Your Dice?",
    status="Are You Rolling with Advantage or Disadvantage?"
)
@app_commands.choices(status=
[
    app_commands.Choice(name="Advantage", value=1),
    app_commands.Choice(name="Disadvantage", value=2),
]
)
async def quickroll(
    interaction: discord.Interaction, 
    sides: Optional[int],
    mod:Optional[int],
    number: Optional[int], 
    status: Optional[app_commands.Choice[int]]
    ):
    
    new_die = d(sides) if sides != None else d(20)

    if status:
        if status.value == 1:
            roll = new_die.roll_adv()
            total = max(roll) + mod if mod != None else max(roll)
            status_text = "*(Advantage)*"
        elif status.value == 2:
            roll = new_die.roll_dis()
            total = min(roll) + mod if mod != None else min(roll)
            status_text = "*(Disadvantage)*"
        
        msg = f'Rolls {status_text}: {roll}\nModifier: {mod}\nTotal: **{total}**' if mod != None else f'Rolls {status_text}: {roll}\nTotal: **{total}**'
    else:
        roll = new_die.roll()
        total = roll + mod if mod != None else roll
        msg = f'Roll: {roll}\nModifier:{mod}\nTotal: **{total}**' if mod != None else f'Roll: **{roll}**'
        
    await interaction.response.send_message(msg)

if __name__ == '__main__':
    client.run(token)
