import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from homework.homework import Homework

class ButtonView(discord.ui.View):
    def __init__(self):
        # making None is important if you want the button work after restart!
        super().__init__(timeout=None)

    # TEXT
    @discord.ui.button(style=discord.ButtonStyle.secondary, label="Set a Reminder:", disabled=True)

    # BUTTON 2
    @discord.ui.button(style=discord.ButtonStyle.blurple, label="in 1 hour")
    async def button2123(self, button, interaction):
        await interaction.message.reply(f"Pinging @{interaction.user} in an hour!")

    # BUTTON 2
    @discord.ui.button(style=discord.ButtonStyle.blurple, label="in 1 hour")
    async def button2(self, button, interaction):
        await interaction.message.reply(f"Pinging @{interaction.user} in an hour!")

    # BUTTON 3
    @discord.ui.button(style=discord.ButtonStyle.blurple, label="7 am")
    async def button3(self, button, interaction):
        await interaction.message.reply(f"Pinging @{interaction.user} tomorrow morning!")

    # BUTTON 4
    @discord.ui.button(style=discord.ButtonStyle.blurple, label="custom")
    async def button4(self, button, interaction):
        await interaction.message.reply("doing the custom things boss!")

class hw(commands.Cog):
    good_guilds = [714354863349170187, 511924606651727895]
    
    @discord.slash_command(guild_ids=good_guilds, name="hw", description="check current homework reminder")
    async def hw(self, ctx):

        title = f"Homework for {ctx.interaction.guild.name}"

        hw = Homework(guild_id = ctx.interaction.guild_id)

        embed = discord.Embed(
            title = title, 
            description = str(hw)
        )

        navigator = ButtonView()

        return await ctx.respond(embed=embed, view=navigator)
            

def setup(bot):
    bot.add_cog(hw(bot))