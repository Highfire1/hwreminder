import discord
#from discord.commands import Option, slash_command
from discord.ext import commands
from discord.ext.commands.context import Context
from discord import slash_command

from homework.homework import Homework

good_guilds = [714354863349170187, 511924606651727895]

class add_hw(commands.Cog):
    @slash_command(
        guild_ids=good_guilds, 
        name="addhw", 
        description="add an assignment to the homework tracker"
    )
    async def add_hw(
        self, ctx, 
        subject: discord.Option(str, "subject"), 
        name: discord.Option(str, "name"), 
        assignment: discord.Option(str, "assignment"), 
        due_date: discord.Option(str, "due date")
    ):
        
        hw = Homework(guild_id = ctx.interaction.guild_id)
        hw.add_assignment(name, subject, assignment, due_date)

        await ctx.respond(f"Added {name} in {subject}.")

def setup(bot):
    bot.add_cog(add_hw(bot))
