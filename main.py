import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import pandas as pd
import random
import webserver

part1_q =""
part1_a =""
part2_q =""
part2_a =""
part3_q =""
part3_a=""
bonusOn=1
edf = pd.read_csv("ebonuses.csv")
mdf = pd.read_csv("mbonuses.csv")
hdf = pd.read_csv("hbonuses.csv")
def newEasyBonus():
    global part1_q, part1_a, part2_q, part2_a, part3_q, part3_a, bonusOn
    random_row = edf.sample(n=1)
    part1_q = random_row["bonus part 1 question"].values[0]
    part1_a = random_row["bonus part 1 answer"].values[0]
    part2_q = random_row["bonus part 2 question"].values[0]
    part2_a = random_row["bonus part 2 answer"].values[0]
    part3_q = random_row["bonus part 3 question"].values[0]
    part3_a = random_row["bonus part 3 answer"].values[0]
    bonusOn = 1
def newMedBonus():
    global part1_q, part1_a, part2_q, part2_a, part3_q, part3_a, bonusOn
    random_row = mdf.sample(n=1)
    part1_q = random_row["bonus part 1 question"].values[0]
    part1_a = random_row["bonus part 1 answer"].values[0]
    part2_q = random_row["bonus part 2 question"].values[0]
    part2_a = random_row["bonus part 2 answer"].values[0]
    part3_q = random_row["bonus part 3 question"].values[0]
    part3_a = random_row["bonus part 3 answer"].values[0]
    bonusOn = 1
def newHardBonus():
    global part1_q, part1_a, part2_q, part2_a, part3_q, part3_a, bonusOn
    random_row = hdf.sample(n=1)
    part1_q = random_row["bonus part 1 question"].values[0]
    part1_a = random_row["bonus part 1 answer"].values[0]
    part2_q = random_row["bonus part 2 question"].values[0]
    part2_a = random_row["bonus part 2 answer"].values[0]
    part3_q = random_row["bonus part 3 question"].values[0]
    part3_a = random_row["bonus part 3 answer"].values[0]
    bonusOn = 1
load_dotenv()
token = os.getenv('DISCORD_TOKEN')  

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("bot is ready")

@bot.command()
async def easybonus(ctx):
    await ctx.send("New Easy Bonus Set")
    newEasyBonus()

@bot.command()
async def mediumbonus(ctx):
    await ctx.send("New Medium Bonus Set")
    newMedBonus()

@bot.command()
async def hardbonus(ctx):
    await ctx.send("New Hard Bonus Set")
    newHardBonus()

@bot.command()
async def read(ctx):
    if bonusOn == 1:
        await ctx.send(part1_q)
    elif bonusOn == 2:
        await ctx.send(part2_q)
    elif bonusOn == 3:
        await ctx.send(part3_q)
    else:
        await ctx.send("bonus finished")

@bot.command()
async def answer(ctx):
    global bonusOn
    if bonusOn == 1:
        await ctx.send(part1_a)
    elif bonusOn == 2:
        await ctx.send(part2_a)
    elif bonusOn == 3:
        await ctx.send(part3_a)
    else:
        await ctx.send("bonus finished")
    bonusOn += 1

@bot.command()
async def commands(ctx):
    await ctx.send("!easybonus - new easy bonus set\n!mediumbonus - new medium bonus set\n!hardbonus - new hard bonus set\n!read - read the next part of the bonus\n!answer - reveal the answer to the last read part of the bonus")

webserver.keep_alive()
bot.run(token,log_handler=handler, log_level=logging.DEBUG)
