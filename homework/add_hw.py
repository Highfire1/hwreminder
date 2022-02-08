import discord
#from discord.commands import Option, slash_command
from discord.ext import commands
from discord.ext.commands.context import Context
from discord import slash_command

from homework.homework import Homework

import dateparser
import time
import difflib

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
        assignment: discord.Option(str, "assignment"), 
        due_date: discord.Option(str, "due date")
    ):
        hw = Homework(guild_id = ctx.interaction.guild_id)
        a = hw.add_assignment(subject, assignment, due_date)

        embed = discord.Embed(
            title = a.subject + " homework created.",
            description = f"{a.assignment}\n\nDue date: {a.due_date}",
        )

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(add_hw(bot))
