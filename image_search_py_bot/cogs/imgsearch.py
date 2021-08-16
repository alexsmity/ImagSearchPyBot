import discord
import os
import random
from discord.ext import commands
from googleapiclient.discovery import build


class work(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def show(self, ctx, *, search):
        ran = random.randint(0, 9)
        resource = build("customsearch",
                         "v1",
                         developerKey=['your google api key']).cse()
        result = resource.list(q=f"{search}",
                               cx="your search engine id ",
                               searchType="image").execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"Here Your Image ({search.title()})")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)


def setup(client):
    client.add_cog(work(client))
