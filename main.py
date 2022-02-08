'''
INVITE LINK: https://discord.com/oauth2/authorize?client_id=896896783123357729&scope=bot&permissions=8
'''
# =============================== #

import discord
from discord.commands import permissions

import os
from dotenv import load_dotenv

import sys

# =============================== #

load_dotenv()

bot = discord.Bot(activity = discord.Game(name="hacking YOUR server :)))))"))

good_guilds = [714354863349170187, 511924606651727895]

# =============================== # 

@bot.event
async def on_ready():
    print(f"\033[1;31;40mBOT STARTED AS {bot.user}\033[0m")

# =============================== #

@bot.slash_command(guild_ids=good_guilds)
@permissions.is_owner()
async def danger(ctx, code: discord.Option(str, "code")):
    command = ctx.interaction.data["options"][0]["value"]
    command = "output: " + str(eval(command))
    await ctx.respond(command)

@bot.slash_command(guild_ids=good_guilds, name = "exit", desc="DANGER: SHUTS DOWN THE BOT")
@permissions.is_owner()
async def exit(ctx):
    await ctx.respond("bye :)")
    sys.exit()

# =============================== #

#bot.load_extension("cogs.cog1")
#bot.load_extension("cogs.cog3")

bot.load_extension("homework.hw")
bot.load_extension("homework.add_hw")

bot.run(os.getenv("TOKEN"))

# =============================== #