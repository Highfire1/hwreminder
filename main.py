'''
INVITE LINK: https://discord.com/oauth2/authorize?client_id=896896783123357729&scope=bot&permissions=8
'''

import discord
from discord.commands import permissions

import os
from dotenv import load_dotenv

load_dotenv()



bot = discord.Bot()

good_guilds = [714354863349170187, 511924606651727895]

@bot.event
async def on_ready():
    print(f"\033[1;31;40mBOT STARTED: {bot.user} \033[0;0")


@bot.slash_command(guild_ids=good_guilds)
@permissions.is_owner()
async def danger(ctx, code: discord.Option(str, "code")):
    command = ctx.interaction.data["options"][0]["value"]
    command = "output: " + str(eval(command))
    await ctx.respond(command)

@bot.slash_command(guild_ids=good_guilds)
async def hw(ctx):
    command = ctx.interaction.data["options"][0]["value"]
    command = "output: " + str(eval(command))
    await ctx.respond(command)

class ButtonView(discord.ui.View):
    def __init__(self):
        # making None is important if you want the button work after restart!
        super().__init__(timeout=None)

    # custom_id is required and should be unique for <commands.Bot.add_view>
    # attribute emoji can be used to include emojis which can be default str emoji or str(<:emojiName:int(ID)>)
    # timeout can be used if there is a timeout on the button interaction. Default timeout is set to 180.
    @discord.ui.button(
        style=discord.ButtonStyle.blurple, custom_id="counter:firstButton"
    )
    async def leftButton(self, button, interaction):
        await interaction.response.edit_message("button was pressed!")

@bot.slash_command(
    guild_ids=good_guilds, name="slash_command_name", description="command description!"
)
async def CommandName(ctx):
    navigator = ButtonView()  # button View <discord.ui.View>
    await ctx.respond("press the button.", view=navigator)

# for error handling
@CommandName.error
async def CommandName_error(ctx, error):
    return await ctx.respond(
        error, ephemeral=True
    )  # ephemeral makes "Only you can see this" message

bot.run(os.getenv("TOKEN"))
