import discord
#from discord.commands import Option, slash_command
from discord.ext import commands
from discord.ext.commands.context import Context

from homework.homework import Homework

class hw(commands.Cog):
    good_guilds = [714354863349170187, 511924606651727895]
    
    @discord.slash_command(guild_ids=good_guilds, name="hw", description="check current homework reminder")
    async def hw(self, ctx):

        hw = Homework(guild_id = ctx.interaction.guild_id)
        return await ctx.respond(f"{ctx.interaction.guild.name}: {hw}", ephemeral=True)

    @hw.error
    async def ping_error(self, ctx: Context, error):
        return await ctx.respond(
            error, ephemeral=True
        )  # ephemeral makes "Only you can see this" message

def setup(bot):
    bot.add_cog(hw(bot))