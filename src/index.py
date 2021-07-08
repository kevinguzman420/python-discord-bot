import discord, datetime
from discord.ext import commands
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="Thisis a helper bot")

client = discord.Client()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="IN GOD'S TIME OF WAITING", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Sever Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    # print(search_results)
    await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])
    
# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
    print("My Bot is Ready")

bot.run('ODYyNDcwMDgwNjA4MDc1ODM2.YOYz2w.b7_Nkg4VAHwJwYGj3XrhfHxtqI8')

