from discord.ext import commands, menus
import re, discord , random , mystbin , typing, emoji, unicodedata, textwrap, contextlib, io

class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief = "gets you a guild's icon", aliases = ["guild_icon"])
  async def server_icon(self, ctx, *, guild : typing.Optional[discord.Guild] = None):
    guild = guild or ctx.guild

    if not guild:
      return await ctx.send("no guild to get the icon of.")
    
    await ctx.send(f"{guild.icon.url}" if guild.icon else "https://i.imgur.com/3ZUrjUP.png")

async def setup(bot):
  await bot.add_cog(Info(bot))