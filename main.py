'''
INVITE LINK: https://discord.com/oauth2/authorize?client_id=896896783123357729&scope=bot&permissions=8
'''
# =============================== #

import discord
from discord.commands import permissions

import os
from dotenv import load_dotenv

# =============================== #

load_dotenv()

bot = discord.Bot()

good_guilds = [714354863349170187, 511924606651727895]

# =============================== #

@bot.event
async def on_ready():
    print(f"\033[1;31;40mBOT STARTED: {bot.user} \033[0m")

# =============================== #

@bot.slash_command(guild_ids=good_guilds)
@permissions.is_owner()
async def danger(ctx, code: discord.Option(str, "code")):
    command = ctx.interaction.data["options"][0]["value"]
    command = "output: " + str(eval(command))
    await ctx.respond(command)

# =============================== #

@bot.slash_command(guild_ids=good_guilds)
async def hw(ctx):
    command = ctx.interaction.data["options"][0]["value"]
    command = "output: " + str(eval(command))
    await ctx.respond(command)

# =============================== #

bot.load_extension("cogs.cog1")

bot.run(os.getenv("TOKEN"))

# =============================== #