import discord
#import discord.ext 
import ClientConfig
import os
import asyncio
import random
import B
import random_response
import imghdr
import aiohttp
import aiodns
from PIL import Image
import chardet
import re
from io import BytesIO
#from itertools import cycle
import requests #do not use unless you know why your doing
import datetime
from pytz import timezone #all good
import pymongo
import discord_webhook
from difflib import SequenceMatcher
import tweepy
import lavalink
#import itertools
import functools
import math
from async_timeout import timeout
from clear_code import clear
import DatabaseControl
import RankSystem
import GlobalLinker
import UpdateNotify
import DatabaseConfig
import urllib3
import numpy as np
import logging
import emojis
from bs4 import BeautifulSoup
import GetPfp
import emote
import color_code
import userinfo
import jdjg_os
import mystbin
import json
today = datetime.date.today()
day = today.strftime('%m/%d/%Y %H:%M:%S')
logging.basicConfig(level=logging.WARNING)
ratelimit_detection=logging.Filter(name='WARNING:discord.http:We are being rate limited.')

#don't delete any import statements - some things might be not used

#All code that has been transfered over took a while.

client = ClientConfig.client

#don't touch the database

time_location = "America/New_York"  #The current timezone.
#DATABASE LOGIN MOVED TO DATABASECONFIG.PY

all_commands = """random_message - is random messages
ad -advice
help is how you get help
Owner(bot makers) has access to change the status - a.k.a with status(it's admin only for safetly reasons)
random_number is random number(ability to choose starting and ending numbers will be added soon...)
time will give you the current bot time
About is who made it
say repeats what you say
support contacts the bot makers in Admin and gets their support(Okay so... well you can choice DM or send it to a certain channel)
mail allows you to send messages to people in Dms soon..
Log off is a command to turn off the bot(admins only)
clear is now avaible(manage messages only...)
Support also includes Suggestions(more features will be added soon)
coin is coin flip try with coin flip <heads or tails> (it will tell you if you're right.>
Webhook updates(JDJG only)

Color to convert values:

use from to values then more

Example:

color hex decimal ff8a00

More commands

Emote(find a emote in the servers the bot is in(might not be that accurate but it's alright)

servers(gives some server info- admins only)

Tweet - gives messages from Usernames

exmaple:


tweet MikeTV 99

webhook - works url then message

example:

webhook <url> hey
------------------------

doesn't work the other way

(might be more):

webhook_create is for creating a webhook

you must Use

webhook_create <name> <reason>

(both are not required anymore, and it will send you a test.)

You must have have an attached image

If you want to use an avatar you will need to attach one to the message

power - get the root of the power so if you do JDBot*square 3 1 it will be 3, and stuff like that(it won't work if you do JDBot*square three one)

radical will be like the number and using radical 3 so if you did 27 it would become 3

Like JDBot*radical 27 3 = 3"""



all_commands2 = """Work is for well seeing how well two things get a long.

(I am not adding a ship command... if I really need to, then ask...)

But it will say who requested the command.

Try the help command and reading the source code for all the features

DMing the bot will send what you send to us.

Database fuctionality is provided by well you can see if you read the source code

If you want a feature, just ask... or try a command and it will send it to us like :

Time setting is now a thing....(so commands will no longer work at a certain time...)

The insult command to insult you, why?

(Fun Fact it will question your ideas.....)

Eh...

compliment is here as well
apply bloopers I would like <role>, <message(reason why)>

Arithmetic <starting_number> <number_multipled each time> <times_multipled>
link_channel
delete_link
GetLinked
GetChannelId
rank
global
"""

commmands_here=[
  "help",
  "random_message",
  "advice",
  "random_number",
  "about/help_2",
  "time",
  "say",
  "support DM ",
  "support channel",
  "mail",
  "clear",
  "rank",
  "lead"
]
admin_commands = [
"log off",
"dev_rank",
"link_channel",
"delete_link",
"global",
"toggle [sub-command]",
"update [sub-command]",
"GetLinked",
"GetChannelId",
"status"
]
commands_discription=[
"The help message you are veiwing right now",
"Sends a random message to the channel that the command was recieved from",
"Gives random advice to you just when you ask for it :)",
"Gives you a random number between a given range",
"Old Help Page",
"Gives the current time in the JDJG time zone!",
"Bot repeats what you say...sort of like a robot!",
"Does nothing for some reason",
"Also does nothing",
"Send mail to your best Discord Friends! Irl or not Irl! Creates a dm containing your mail to the specified user",
"Clears the last thing you said in that channel",
"Displays your current rank in the server as well as all linked servers",
"Shows the leaderboard for the rank system. Use JDBot*lead local for server leaderboards and JDBot*lead global for the leaderboard for all connected servers"
]
admin_commands_discription =[
  "Turns off JDJG bot for all servers",
  "Gets the rank of the specified user",
  "Merge two channels from any server into one combined chat room",
  "Delete a linked channel from any channel or server",
  "Defines a global channel that can be merged with all other servers global channel so that users can partisipate in a global chat room",
  "Toggles JDBot Settings such as level up messages!",
  "Notify people about important events that are happening in your server!",
  "Get all channels linked to the current Channel",
  "Gets the current channel Id",
  "JDBot goes into sleep mode and displays no custom status for 5 seconds?"
]
admin_commands_usage_discription=[
"JDBot*log off",
"JDBot*dev_rank USERNAME_NO_DISCRIMINATOR",
"JDBot*link_channel CHANNEL1_ID CHANNEL2_ID",
"JDBot*delete_link CHANNEL1_ID CHANNEL2_ID",
"JDBot*global",
"JDBot*toggle level_msg",
"JDBot*update [sub-subcommand] <sub commands are : title,body_head, body, preview,set,send>",
"JDBot*GetLinked",
"JDBot*GetChannelId",
"JDBot*status"
]
bad_value = [
  "",
  " ",
]

#commmands_here = commands that the code can currently do

jdjg_id = [
  168422909482762240,
  393511863385587712,

]

url_collection = []

#this is used for the order command

#jdjg's id only(don't add any more)

async def status_task():
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=" JDBot*help"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers | {len(client.users)} users"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="with Repl.it"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="the creators:"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Nomic Zorua"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="JDJG and Shadi"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="RenDev and LinuxTerm"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="JDJG Bot will DM you two servers join if you want help from the bot makers - from about command or help command"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="(the first one is the support server), though the blooper server will tend to do it now - second one"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="use JDBot!help for the test commands"))
        await asyncio.sleep(30)
        

#be careful not to have a * anywhere else,
#or the text will be italicised

discordprefix = "JDBot*"

guild_prefixes = {}

##Replace admins with your user ids on discord for you to be admins, and the help commands with your prefix, basically replace JDBot* with your prefix of choice if you want to.

async def startup():
  await client.wait_until_ready()
  client.os_user = "None"
  client.check_users = {}
  #client.lavalink=await asyncio.create_subprocess_shell('java -jar Lavalink.jar')
  await status_task()

@client.event
async def on_ready():
  print("Bot is ready.\n")

async def help(message):
  if (message.author.dm_channel is None):
    await message.author.create_dm()
  embedVar2 = discord.Embed(title="User Commands",color=random.randint(0, 16777215))
  i=-1
 # print(len(commmands_here))
  #print(len(commands_discription))
  for x in commmands_here:
    i=i+1
    #print(i)
    embedVar2.add_field(name=x,value=commands_discription[i],inline=True)
  await message.author.dm_channel.send(embed=embedVar2)
  if message.author.id in admins:
    embedVar1 = discord.Embed(title="Admin Commands",color=random.randint(0, 16777215))
    i=-1
    #print(len(admin_commands))
    #print(len(admin_commands_usage_discription))
    for x in admin_commands:
      i=i+1
      embedVar1.add_field(name=x,value=admin_commands_discription[i]+" usage: "+admin_commands_usage_discription[i],inline=True)
    await message.author.dm_channel.send(embed=embedVar1)

  return
    

admins = [
  168422909482762240,
  269904594526666754,
  717822288375971900,
  357006546674253826,
  734666800905846834,
]

admin_contact = [
  168422909482762240,
  717822288375971900,
  357006546674253826,

]

#adding an id(if you have access to the source code and want to fork it, credit us, getting your discord id is easy, replace ours with the ones you are playing to use)

send_channel = [
  556242984241201167, 
  738912143679946783, 
]

safe_servers = [736422329399246990, 736966204606120007,736051343185412296]

slur_okay = [736051343185412296,745559622856998953,643960606998790154]

from_to_channel={}

@client.event
async def on_guild_join(guild_fetched):
  channels = [channel for channel in guild_fetched.channels]

  roles = roles= [role for role in guild_fetched.roles]

  embed = discord.Embed(title="Bot just joined: "+str(guild_fetched.name), color=random.randint(0,16777215))
  embed.set_thumbnail(url = guild_fetched.icon_url)
  embed.add_field(name='Server Name:',value=f'{guild_fetched.name}')
  embed.add_field(name='Server ID:',value=f'{guild_fetched.id}')
  embed.add_field(name='Server region:',value=f'{guild_fetched.region}')
  embed.add_field(name='Server Creation Date:',value=f'{guild_fetched.created_at}')
  embed.add_field(name='Server Owner:',value=f'{guild_fetched.owner}')
  embed.add_field(name='Server Owner ID:',value=f'{guild_fetched.owner.id}')
  embed.add_field(name='Member Count:',value=f'{guild_fetched.member_count}')
  embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
  embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
  await client.get_channel(738912143679946783).send(embed=embed)

#Typing Status Support
waitMessage = 0
#commands with embed: help, mail, support, about, update(will soon)
@client.event
async def on_message(message):
  #await GlobalLinker.respond(message)
  global url_collection
  global safe_servers
  global waitMessage
  user = message.author

  if client.user in message.mentions and not message.author.bot:
    embed = discord.Embed(title="Mention info:",description="Tip: you can disable level up messages with JDBot*toggle level_msg \nNow converting mention into a command.",color=random.randint(0, 16777215))
    await message.channel.send(embed=embed)
    replace_value = (f"<@!{client.user.id}> ")
    message.content=message.content.replace(replace_value, discordprefix)
    message.mentions.remove(client.user)

  if client.user in message.mentions and not message.author.bot and "shut up " in (message.content.lower()+" "):
    await message.channel.send("I try to help you know")

  if message.content.startswith(discordprefix+" ") and not message.author.bot:
    message_info=message.content.split(" ")
    while '' in message_info:
      message_info.remove('')
    if len(message_info) > 0:
      x = 2
      message.content = message_info[0]+message_info[1]
      while x < (len(message_info)):
        if x == (len(message_info)-1):
          message.content = (message.content+" "+message_info[-1])
        else:
         message.content = (message.content+" "+message_info[x])
        x = x + 1
      
      x = 0

  message_check=re.findall(rf"{discordprefix}[{discordprefix}]",message.content, flags=re.IGNORECASE)
  if len(message_check) > 0:
    check_time=message_check[0]
    if check_time.lower() == discordprefix.lower():
      message.content = message.content.replace(check_time,discordprefix)
    
  if message.reference != None and not message.content.startswith(discordprefix) and not message.author.bot:
    return
    
  if message.guild is None and not message.author.bot and not message.content.startswith(discordprefix):
    punc = [' ','.','!','?']
    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("sus","")
    for pun in punc:
      tmpStr = tmpStr.replace("sus"+pun,"")
    check_sus = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("shut up","")
    for pun in punc:
      tmpStr = tmpStr.replace("shut up"+pun,"")
    shut_up = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("hello","")
    for pun in punc:
      tmpStr = tmpStr.replace("hello"+pun,"")
    hello_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("hi","")
    for pun in punc:
      tmpStr = tmpStr.replace("hi"+pun,"")
    hi_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("hey all","")
    for pun in punc:
      tmpStr = tmpStr.replace("hey all"+pun,"")
    hey_all_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("sup","")
    for pun in punc:
      tmpStr = tmpStr.replace("sup"+pun,"")
    sup_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("what's up","")
    for pun in punc:
      tmpStr = tmpStr.replace("what's up"+pun,"")
    what_up_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("chips","")
    for pun in punc:
      tmpStr = tmpStr.replace("chips"+pun,"")
    jdjg_chip_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("reverse","")
    for pun in punc:
      tmpStr = tmpStr.replace("reverse"+pun,"")
    reverse_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("spam","")
    for pun in punc:
      tmpStr = tmpStr.replace("spam"+pun,"")
    spam_check = (len(message.content)!=len(tmpStr))

    tmpStr = message.content.lower()
    tmpStr = tmpStr.replace("paradox","")
    for pun in punc:
      tmpStr = tmpStr.replace("paradox"+pun,"")
    paradox_check = (len(message.content)!=len(tmpStr))

     
    if (spam_check):
      try:
        await message.channel.send("https://tenor.com/view/shoot-spam-gif-11220664")
      except:
        pass
    
    if (paradox_check):
      try:
        await message.channel.send("https://tenor.com/view/nasa-nasa-gifs-black-hole-nasagif-gif-10093312")
      except:
        pass


    if (check_sus):
      await message.channel.send("You sus for saying sus.")
    if (shut_up):
      pfp=message.author.avatar_url
      time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
      await message.channel.send("Can you not? I am here to help you out. Telling me to shut up is not nice!")
      embed_message = discord.Embed(title="they told me to shut up :(",description=time_used,color=random.randint(0, 16777215),timestamp=datetime.datetime.utcnow())
      embed_message.set_author(name=f"The user known as {message.author}",icon_url=(pfp))
      embed_message.set_thumbnail(url = "https://cdn.discordapp.com/emojis/738514652664955012.png")
      embed_message.set_footer(text = f"{message.author.id}")
      channel_usage=client.get_channel(738912143679946783)
      embed_message.add_field(name="Sent To:",value=str(channel_usage))
      await channel_usage.send(embed=embed_message)
    if (hello_check):
      await message.add_reaction("<a:mariodance:738972099460202567>")
    if (hi_check):
      if message.content == "hi" or "hi " in message.content:
        try:
          await message.add_reaction("<a:mariodance:738972099460202567>")
        except:
          pass

    if (hey_all_check):
      try:
        await message.add_reaction("<a:mariodance:738972099460202567>")
      except:
        pass

    if(sup_check):
      try:
        await message.add_reaction("<a:mariodance:738972099460202567>")
      except:
        pass

    if(what_up_check):
      try:
        await message.channel.send("It depends on your perception of up, but I suggest you rephase the statement.")
      except:
        pass
    
    if(jdjg_chip_check):

      try:
        await message.add_reaction("<:JDJGooh:737913423853256784>")
        await message.channel.send("ooh chips.")
      except:
        pass

    if (reverse_check):
      try:
        file = discord.File("reverse.png")
        await message.channel.send("Your reverse card was banned." ,file=file)
      except:
        pass
    
    else:

      pfp=message.author.avatar_url

      time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')


      embed_message = discord.Embed(title=message.content, description=time_used, color=random.randint(0, 16777215))
      
      embed_message.set_author(name=f"Direct Message From {message.author}:",icon_url=(pfp))
      embed_message.set_footer(text = f"{message.author.id}")

      embed_message.set_thumbnail(url = "https://media.discordapp.net/attachments/556242984241201167/763866804359135292/inbox.png?width=677&height=677")

      channel_usage=client.get_channel(738912143679946783)
      embed_message.add_field(name="Sent To:",value=str(channel_usage))
      await channel_usage.send(embed=embed_message)
    return

  if not message.guild is None and not message.author.bot:

    if message.guild.id in guild_prefixes and not message.author.bot:
      server_prefix=guild_prefixes[message.guild.id]
      if message.content.startswith(server_prefix):
        message.content = message.content.replace(server_prefix,discordprefix)
        print(message.content)

    if message.guild.id == 731732168602288199 and not message.author.bot:
      punc = [' ','.','!','?']
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("yoshicake","")
      for pun in punc:
        tmpStr = tmpStr.replace("yoshicake"+pun,"")
      yoshicake_check = (len(message.content)!=len(tmpStr))

      if (yoshicake_check):
        try:
          await message.channel.send("https://tenor.com/view/birthday-faded-marion-cartoons-cake-gif-4878378")
        except:
          pass

    if message.guild.id in safe_servers and not message.author.bot and not message.content.startswith(discordprefix):
      punc = [' ','.','!','?']
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("sus","")
      for pun in punc:
        tmpStr = tmpStr.replace("sus"+pun,"")
      check_sus = (len(message.content)!=len(tmpStr))
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("hello","")
      for pun in punc:
        tmpStr = tmpStr.replace("hello"+pun,"")
      hello_check = (len(message.content)!=len(tmpStr))
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("hi","")
      for pun in punc:
        tmpStr = tmpStr.replace("hi"+pun,"")
      hi_check = (len(message.content)!=len(tmpStr))
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("reverse","")
      for pun in punc:
        tmpStr = tmpStr.replace("reverse"+pun,"")
      reverse_check = (len(message.content)!=len(tmpStr))
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("hey all","")
      for pun in punc:
        tmpStr = tmpStr.replace("hey all"+pun,"")
      hey_all_check = (len(message.content)!=len(tmpStr))
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("sup","")
      for pun in punc:
        tmpStr = tmpStr.replace("sup"+pun,"")
      sup_check = (len(message.content)!=len(tmpStr))
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("chips","")
      for pun in punc:
        tmpStr = tmpStr.replace("chips"+pun,"")
      chips_check = (len(message.content)!=len(tmpStr))

      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("what's up","")
      for pun in punc:
        tmpStr = tmpStr.replace("what's up"+pun,"")
      what_up_check = (len(message.content)!=len(tmpStr))
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("sup","")
      for pun in punc:
        tmpStr = tmpStr.replace("sup"+pun,"")
      sup_check = (len(message.content)!=len(tmpStr))

      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("spam","")
      for pun in punc:
        tmpStr = tmpStr.replace("spam"+pun,"")
      spam_check = (len(message.content)!=len(tmpStr))

      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("paradox","")
      for pun in punc:
        tmpStr = tmpStr.replace("paradox"+pun,"")
      paradox_check = (len(message.content)!=len(tmpStr))

      if (paradox_check):
        try:
          await message.channel.send("https://tenor.com/view/nasa-nasa-gifs-black-hole-nasagif-gif-10093312")
        except:
          pass
     

      if (spam_check):
        try:
          await message.channel.send("https://tenor.com/view/shoot-spam-gif-11220664")
        except:
          pass

      if (check_sus):
        try:
          await message.channel.send("You sus for saying sus.")
        except:
          pass

      if (hello_check):
        try:
          await message.add_reaction("<a:mariodance:738972099460202567>")
        except:
          pass 

      if (hi_check):
        if message.content == "hi" or "hi " in message.content:
          try:
            await message.add_reaction("<a:mariodance:738972099460202567>")
          except:
            pass

      if(reverse_check):
        try:
          file = discord.File("reverse.png")
          await message.channel.send("Your reverse card was banned." ,file=file)
        except:
          pass

      if (hey_all_check):
        try:
          await message.add_reaction("<a:mariodance:738972099460202567>")
        except:
          pass

      if (sup_check):
        try:
          await message.add_reaction("<a:mariodance:738972099460202567>")
        except:
          pass

      if(chips_check):
        try:
          await message.add_reaction("<:JDJGooh:737913423853256784>")
          await message.channel.send("ooh chips.")
        except:
          pass

      if (what_up_check):
        try:
          await message.channel.send("It depends on your perception of up, but I suggest you rephase the statement.")
        except:
          pass

      if (sup_check):
        try:
          await message.add_reaction("<a:mariodance:738972099460202567>")
        except:
          pass

  if message.content.startswith(discordprefix+"verify") and not message.author.bot:
    if message.guild != None:
      if message.guild.id == 736422329399246990:
        if message.channel.id == 736432046821343322:
          await message.channel.send("Vertification time...")
          member_role = message.guild.get_role(736423134449893428)
          await message.author.add_roles(member_role,reason="User Vertification by Bot.")
          return
      if message.guild.id == 748631738908934211:
        if message.channel.id == 779407591511818303:
          await message.channel.send("Vertification time...")
          member_role = message.guild.get_role(748654102040412291)
          await message.author.add_roles(member_role,reason="User Vertification by Bot.")
          member_role = message.guild.get_role(748640407201644624)
          await message.author.add_roles(member_role,reason="User Vertification by Bot.")
          return

  if message.content.startswith(discordprefix+"text_backup") and not message.author.bot:
    if len(message.attachments) > 0:
      if (message.attachments[0].url).endswith(".txt"):
        info=await message.attachments[0].read()
        if len(info) > 0:
          the_encoding = chardet.detect(info)['encoding']
          text=info.decode(the_encoding)
          mystbin_client = mystbin.MystbinClient()
          paste = await mystbin_client.post(text)
          await message.channel.send("added text file to mystbin")
          await message.channel.send(paste.url)
          await mystbin_client.close()
        if len(info) == 0:
          await message.channel.send("it's not going to work with 0 bytes.")
      if not (message.attachments[0].url).endswith(".txt"):
        await message.channel.send("That's not a .txt file.")
    if len(message.attachments) == 0:
      await message.channel.send("Please try actually uploading a text file.")
    return
  
  if message.content.startswith(discordprefix+"look_at") and not message.author.bot:
    emoji_list=message.guild.emojis
    message_emojis = ""
    for x in emoji_list:
      if x.animated == True:
        message_emojis = message_emojis+" "+str(x)
    await message.channel.send(message_emojis)
    return
  
  if message.content.startswith(discordprefix+"CRAP_BACKUP") and not message.author.bot:
    await message.channel.send("Crap ok...ill back them up real quick")
    guild_search = client.get_guild(736422329399246990)
    guild_emoji_fetch = guild_search.emojis
    for obj in guild_emoji_fetch:
      img = await obj.url.read()
      from PIL import Image
      import io
      print(obj.name)
      image_data = img
      image = Image.open(io.BytesIO(image_data))
      if(str(obj.url).replace(".png","")!=str(obj.url)):
        image.save("./backup/"+obj.name+".png","png");
      if(str(obj.url).replace(".gif","")!=str(obj.url)):
        from PIL import Image, ImageSequence
        index = 1
        frames = []
        for frame in ImageSequence.Iterator(image):
          frames.append(frame)
        frames[0].save("./backup/"+obj.name+".gif", format='GIF', append_images=frames[1:], save_all=True)
      #
    await message.channel.send("That was close but it is all backed up to disk :)")
    return

  if message.content.startswith(discordprefix+"ping") and not message.author.bot:
    await message.channel.send("Pong")
    await message.channel.send(f"Response time: {client.latency*1000}")
    return

  if message.content.startswith(discordprefix+"pi") and not message.author.bot:
    await message.channel.send(math.pi)
    return

  if message.content.startswith(discordprefix+"test") and not message.author.bot:
    return 

  if message.content.startswith(discordprefix+"pat") and not message.author.bot:
    return

  if message.content.startswith(discordprefix+"email") and not message.author.bot:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    if len(message.content.split(" ")) == 1:
      await message.channel.send("Not enough arguments")
      return

    return
  
  if message.content.startswith(discordprefix+"triggered") and not message.author.bot:
    if len(message.attachments) > 0:
      if message.attachments[0].filename.endswith(".png"):
        url = message.attachments[0].url
      else:
        url = message.author.avatar_url
    
    if len(message.attachments) == 0:
      url = message.author.avatar_url_as(format="png")
    
    async with aiohttp.ClientSession() as cs:
      async with cs.get(f"https://some-random-api.ml/canvas/triggered?avatar={url}") as anime:
        image= BytesIO(await anime.read())
      file=discord.File(image, "triggered.gif")
      await message.channel.send(file=file)
    return

  if message.content.startswith(discordprefix+"mchistory") and not message.author.bot:
    username = message.content.replace(discordprefix+"mchistory","")
    if username == (""):
      username = "JDJG_IncOfficial"
    async with aiohttp.ClientSession() as cs:
      async with cs.get(f'https://some-random-api.ml/mc?username={username}') as anime:
        res = await anime.json()
    for x in res:
      if x == "error":
        await message.channel.send(res[x])
        return

    minecraft_uuid = res["uuid"]
    minecraft_username = res["username"]
    embed=discord.Embed(title=f"Minecraft Username: {minecraft_username}",color=random.randint(0, 16777215))
    embed.set_footer(text=f"Minecraft UUID: {minecraft_uuid}")
    value = 0
    for x in(res["name_history"]):
      if value > 0:
        username = (x["name"])
        date_happened = x["changedToAt"]
        embed.add_field(name=f"Username:\n{username}",value=f"Date Changed:\n{date_happened}")
      if value == 0:
        info=x["changedToAt"]
        embed.add_field(name=f"{info}:",value=x["name"])
      value = value + 1

    embed.set_author(name=f"Requested by {message.author}",icon_url=(message.author.avatar_url))
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"wink") and not message.author.bot:
    wink = message.content.replace(discordprefix+"wink","")

    if wink == (""):
      person = client.user
      target = message.author
      
    if len(message.mentions) > 0:
      target = message.mentions[0]
      person = message.author

    if len(message.mentions) == 0:
      person = message.author
      target=await userinfo.user_grab(message)

    if target.id == person.id:
      person = client.user
      target = message.author

    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://some-random-api.ml/animu/wink') as anime:
        res = await anime.json()

    for x in res:
      embed=discord.Embed(color=random.randint(0, 16777215))
      embed.set_author(name=f"{person} winked at you",icon_url=(person.avatar_url))
      embed.set_image(url=res[x])
      await message.channel.send(content=target.mention,embed=embed)
    return

  if message.content.startswith(discordprefix+"facepalm") and not message.author.bot:
    facepalm = message.content.replace(discordprefix+"facepalm","")
    if facepalm == (""):
      person = client.user
      target = message.author
      
    if len(message.mentions) > 0:
      target = message.mentions[0]
      person = message.author

    if len(message.mentions) == 0:
      person = message.author
      target=await userinfo.user_grab(message)

    if target.id == person.id:
      person = client.user
      target = message.author

    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://some-random-api.ml/animu/face-palm') as anime:
        res = await anime.json()

    for x in res:
      embed=discord.Embed(color=random.randint(0, 16777215))
      embed.set_author(name=f"{person} facepalmmed to an action from you",icon_url=(person.avatar_url))
      embed.set_image(url=res[x])
      await message.channel.send(content=target.mention,embed=embed)
    return

  
  if message.content.startswith(discordprefix+"headpat") and not message.author.bot:
    head_pat = message.content.replace(discordprefix+"headpat","")
    if head_pat == (""):
      person = client.user
      target = message.author
      
    if len(message.mentions) > 0:
      target = message.mentions[0]
      person = message.author

    if len(message.mentions) == 0:
      person = message.author
      target=await userinfo.user_grab(message)

    if target.id == person.id:
      person = client.user
      target = message.author

    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://some-random-api.ml/animu/pat') as anime:
        res = await anime.json()

    for x in res:
      embed=discord.Embed(color=random.randint(0, 16777215))
      embed.set_author(name=f"{person} patted you",icon_url=(person.avatar_url))
      embed.set_image(url=res[x])
      await message.channel.send(content=target.mention,embed=embed)
    return

  if message.content.startswith(discordprefix+"hug") and not message.author.bot:
    hug = message.content.replace(discordprefix+"hug","")
    if hug == (""):
      person = client.user
      target = message.author
    
    if len(message.mentions) > 0:
      target = message.mentions[0]
      person = message.author
    
    if len(message.mentions) == 0:
      person = message.author
      target=await userinfo.user_grab(message)

    if target.id == person.id:
      person = client.user
      target = message.author

    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://some-random-api.ml/animu/hug') as anime:
        res = await anime.json()
    for x in res:
      embed=discord.Embed(color=random.randint(0, 16777215))
      embed.set_author(name=f"{person} hugged you",icon_url=(person.avatar_url))
      embed.set_image(url=res[x])
      await message.channel.send(content=target.mention,embed=embed)
    return

  if message.content.startswith(discordprefix+"save_image") and not message.author.bot and message.author.id in jdjg_id:
    if len(message.attachments) > 0:
      obj = message.attachments[0]
      file_name=obj.filename
      url = await obj.save(f"speacil_images/{file_name}",seek_begin=True,use_cached=False)
    return

  if message.content.startswith(discordprefix+"console") and not message.author.bot and message.author.id in jdjg_id:
    command=message.content.replace(discordprefix+"console","")
    run_command=eval(command)
    embed_message = discord.Embed(title=f"{command}",color=random.randint(0, 16777215))
    embed_message.set_author(name=f"Command ran by {message.author}:",icon_url=(message.author.avatar_url))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.add_field(name="result:",value=run_command)
    if (message.author.dm_channel is None):
      await message.author.create_dm()
    await message.author.send(embed=embed_message)
    return

  if message.content.startswith(discordprefix+"mention") and not message.author.bot and user.guild_permissions.administrator == True and message.guild.id in safe_servers:
    user_id=await GetPfp.get_username(message)
    if not user_id == 0:
      pass
    if user_id == 0:
      user_id=message.content.replace(discordprefix+"mention ","")
      try:
        user_id=int(user_id)
      except:
        user_id = message.author.id
    user_there=client.get_user(user_id)
    if user_there == None:
      user_there = message.author
    await message.channel.send(f"{user_there.mention}")
    
    return

  if message.content.startswith(discordprefix+"safe") and not message.author.bot and user.guild_permissions.administrator == True:
    safe_servers.append(message.guild.id)
    return

  if message.content.startswith(discordprefix+"unsafe") and not message.author.bot and user.guild_permissions.administrator == True:
    safe_servers.remove(message.guild.id)
    return


  #await bot.send_typing(ctx.channel)
  #CHANNEL LINKER COMMANDS
  if not message.author.bot: #Channel Link Message Repeater
    if not message.content.startswith(discordprefix):
      if (waitMessage==1):
        await GlobalLinker.TestGLink(message)
        waitMessage = 0
      await RankSystem.UpdateScore(message) #For the rank 
      await GlobalLinker.SendMessage(message)
      await GlobalLinker.extend(message)
      for chanId in DatabaseControl.GetLinkedChannelsList(message.channel.id):
        await client.get_channel(chanId).send(embed=GlobalLinker.GetGlobalEmbed(message))
  if message.content.startswith(discordprefix+"GetChannelId") and not message.author.bot:
    await message.channel.send(message.channel.id)
    return
  if message.content.startswith(discordprefix+"link_this") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    DatabaseControl.AddChannelLink(message.channel.id,n1)
    await message.channel.send("This channel was linked to "+ str(client.get_channel(n1)))
    return   
  if message.content.startswith(discordprefix+"link_channel") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    n2 = str(message.content.split(" ")[2])
    n2 = DatabaseControl.to_ChannelId(n2)
    await message.channel.send(DatabaseControl.AddChannelLink(n1,n2))
    return
  if message.content.startswith(discordprefix+"delete_link") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    n2 = str(message.content.split(" ")[2])
    n2 = DatabaseControl.to_ChannelId(n2)
    await message.channel.send(DatabaseControl.DeleteChannelLink_ChanNum(n1,n2))
    return
  if message.content.startswith(discordprefix+"GetLinked") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    await message.channel.send(DatabaseControl.GetLinkedChannels(client,n1))
    return
  if message.content.startswith(discordprefix+"global_list") and not message.author.bot:
    i=0
    embedVar = discord.Embed(title = "Gobal Channels List",color=random.randint(0, 16777215))
    for obj in DatabaseConfig.db.g_link_testing.find():
      i=i+1
      header = str(i) + ": "
      try:
        header = header +str(client.get_guild(obj["ser_id"]).name)
        body  = str(client.get_channel(obj["chan_id"]).name)
      except:
        header = header + "Cannot Connect"
        body = "<#"+str(obj["chan_id"])+">"
      embedVar.add_field(name = header,value = body)
    await message.channel.send(embed = embedVar)
    return
  if message.content.startswith(discordprefix+"global_mention") and not message.author.bot:
    i=0
    embedVar = discord.Embed(title = "Gobal Channels List",color=random.randint(0, 16777215))
    for obj in DatabaseConfig.db.g_link_testing.find():
      i=i+1
      header = str(i) + ": "
      try:
        header = header +str(client.get_guild(obj["ser_id"]).name)
        body  = str(client.get_channel(obj["chan_id"]).mention)
      except:
        header = header + "Cannot Connect"
        body = "<#"+str(obj["chan_id"])+">"
      embedVar.add_field(name = header,value = body)
    await message.channel.send(embed = embedVar)
    return
#RANK SYSTEM COMMANDS
  if message.content.startswith(discordprefix+"rank") and not message.author.bot:
    await RankSystem.GetStatus(message)
    #await message.channel.send(RankSystem.CheckIfExisting(user))
    return
  if message.content.startswith(discordprefix+"dev_rank") and not message.author.bot:
    await RankSystem.DevGetStatus(client,message)
    #await message.channel.send(RankSystem.CheckIfExisting(user))
    return
  if message.content.startswith(discordprefix+"get_user") and not message.author.bot:
    await message.channel.send("Searching for User")
    await message.channel.send(await GetPfp.get_username(message))
    await message.channel.send("Done!")
    return
  if message.content.startswith(discordprefix+"lead") and not message.author.bot:
    await RankSystem.GetTop10(client,message)
    return
  if message.content.startswith(discordprefix+"toggle") and not message.author.bot:
    args = message.content.split(" ")[1]
    if args == "level_msg":
      await message.channel.send(RankSystem.ToggleLevelUpMsg(message))
    return
#GLOBAL LINKER
  if message.content.startswith(discordprefix+"global") and not message.author.bot:
    args = "NULL"
    try:
      args = message.content.split(" ")[1]
    except:
      await message.channel.send("Did not input an argument!")
    if(args=="link"):
      await message.channel.send(GlobalLinker.AddGlobalLink(client,message))
      return
    if(args=="delete"):
      await message.channel.send(GlobalLinker.TerminateLink(message))
      return
    if(args=="test"):
      await message.channel.send("Next Message sent here will be used as test data")
      waitMessage = 1
      return
    await message.channel.send("Valid arguments are link or delete")
    return
#UPDATE NOTIFY
  if message.content.startswith(discordprefix+"update") and message.author.id in admins and not message.author.bot:
    await UpdateNotify.UpdateNote(message,client)
    
    return

  if message.content.startswith(discordprefix+"help_2") and not message.author.bot:

    #Old help message replaced with new one above ^^^. If you are sad that the old help message is gone, please contact RenDev and he will listen to your dispute

    if (message.author.dm_channel is None):
      await message.author.create_dm()

    await message.author.dm_channel.send("Help is on the way!")

    helpmsg = "prefix is JDBot*, commands are:\n "+all_commands
    embed_message = discord.Embed(title="About(commands):", description=helpmsg, color=random.randint(0, 16777215))
    await message.author.dm_channel.send(embed=embed_message)

    helpmsg2 = "prefix is JDBot*, More commands are:\n "+all_commands2

    embed_message = discord.Embed(title="About(commands):",description=helpmsg2, color=random.randint(0, 16777215))

    await message.author.dm_channel.send(embed=embed_message)
  
    embed_message = discord.Embed(title="About(legal):",description=legal_info, color=random.randint(0, 16777215))

    await message.author.dm_channel.send(embed=embed_message)

    return

#OTHER STUFF
  if message.content.startswith(discordprefix+"help") and not message.author.bot:
    await help(message)
    return

  if message.content.startswith(discordprefix+"random_message") and not message.author.bot:
    message_generator = random.choice(random_response.random_message)
    embed = discord.Embed(title = "Random Message Time...",description=f"**{message_generator}**",color=random.randint(0, 16777215))
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"closest_channel") and not message.author.bot:
    user_wanted = message.content.replace(discordprefix+"closest_channel","")
    channel_used=sorted(message.guild.channels, key=lambda x: SequenceMatcher(None, x.name, user_wanted).ratio())[-1]
    await message.channel.send(channel_used.mention)
    return

  if message.content.startswith(discordprefix+"closest_user") and not message.author.bot:
    guild_fetch = client.get_guild(message.guild.id)
    user_wanted = message.content.replace(discordprefix+"closest_user","")
    userNearest = sorted(client.users, key=lambda x: SequenceMatcher(None, x.name, user_wanted).ratio())[-1]
    await message.channel.send(userNearest)
    userNearest_nick = sorted(client.users, key=lambda x: SequenceMatcher(None, x.display_name,user_wanted).ratio())[-1]
    await message.channel.send(userNearest_nick)
    clean_member_list = []
    for x in guild_fetch.members:
      if x.nick == None:
        pass
      if not x.nick == None:
        clean_member_list.append(x)

    userNearest_server_nick = sorted(clean_member_list, key=lambda x: SequenceMatcher(None, x.nick,user_wanted).ratio())[-1]
    await message.channel.send(userNearest_server_nick)
    return

  if message.content.startswith(discordprefix+"team") and not message.author.bot:
    information=await client.application_info()
    if information.team == None:
      true_owner=information.owner
      team_members = []
    if information.team != None:
      true_owner = information.team.owner
      team_members = information.team.members
    embed=discord.Embed(title=information.name,color=random.randint(0, 16777215))
    embed.add_field(name="Owner",value=true_owner)
    embed.set_footer(text=f"ID: {true_owner.id}")
    embed.set_image(url=(information.icon_url))
    for x in team_members:
      embed.add_field(name=x,value=x.id)
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"owner") and not message.author.bot:
    information=await client.application_info()
    if information.team == None:
      true_owner=information.owner.id
    if information.team != None:
      true_owner = information.team.owner_id
    user99 = client.get_user(true_owner)
    if user99 == None:
      await client.fetch_user(true_owner)
    guild_used=message.guild
    user99_plus=guild_used.get_member(user99.id)
    avatar99 = user99.avatar_url
    bot_decide = user99.bot
    #if it's a bot(bool expression)
    if bot_decide == True:
      user_type = "Bot"
    if bot_decide==False:
      user_type = "User"
    #user_type will become useful later.
    user_id=str(user99.id)
    try:
      joined_guild = user99_plus.joined_at.strftime('%m/%d/%Y %H:%M:%S')
    except:
      joined_guild = "N/A"
    user_create = user99.created_at.strftime('%m/%d/%Y %H:%M:%S')
    try:
      user_status=str(user99.status)
    except:
      user_status = "NULL"
    user_status = user_status.upper()
    try:
      nickname = str(user99_plus.nick)
    except:
      nickname = "None"
    x = 0
    try:
      while x < len(user99_plus.roles):
        x = x + 1
      highest_role=user99_plus.roles[x-1]
    except:
      highest_role = "N/A"
    guild_list = " "
    for guild in client.guilds:
      if user99 in guild.members:
        guild_list+=(", "+guild.name)
    if guild_list == " ":
      guild_list = "Null"

    #user_level = int(DatabaseConfig.db.users_testing.find_one({"user_id":user99.id})["level"])
    #user_local_rank = RankSystem.GetRank(user99,message.guild)
    #user_global_rank = RankSystem.GetRank(user99)
    embedVar = discord.Embed(title=str(user99),description=user_type, color=random.randint(0, 16777215))
    embedVar.set_image(url=avatar99)
    embedVar.add_field(name="Owner: ", value = user99.name)
    embedVar.add_field(name="Nickname: ", value = nickname)
    embedVar.add_field(name="Joined Discord: ",value = user_create)
    embedVar.add_field(name="Joined Guild: ",value = joined_guild)
    embedVar.add_field(name="Part of Guilds:", value=guild_list)
    embedVar.add_field(name="ID:",value=user_id)
    embedVar.add_field(name="Status:",value=user_status)
    embedVar.add_field(name="Highest Role:",value=highest_role)
    #embedVar.add_field(name="Level: ",value = user_level)
    #embedVar.add_field(name="Global Rank: ",value=user_global_rank)
    #embedVar.add_field(name="Local Rank: ",value=user_local_rank)
    await message.channel.send(embed=embedVar)
    try:
      await RankSystem.GetStatus(message,user99 )
    except:
      await message.channel.send("User not in Rank System")
    #turn these into embed info stuff. hash check will just an embed image(so feel free to delete hash_check i-tself, but keep avatar99, or at least the stuff to get it.)
    return
    return
  if message.content.startswith(discordprefix+"fetch_guild"):

    id_used = message.content.replace(discordprefix+"fetch_guild ","")

    value = 0

    try:

      id_used=int(id_used)

    except:

      for guild in client.guilds:
        if  id_used == guild.name:

          id_used = guild.id

          value = "Yes"

        else:

          value = None

      
        if value == None:
          id_used = message.guild.id
    
    guild_fetched = client.get_guild(id_used)

    if guild_fetched == None:

      guild_fetched = client.get_guild(message.guild.id)

    channels = [channel for channel in guild_fetched.channels]
    roles = [role for role in guild_fetched.roles]
    embed = discord.Embed(title="Guild Info", color=random.randint(0, 16777215))
    embed.set_thumbnail(url = guild_fetched.icon_url)
    embed.add_field(name='Server Name:',value=f'{guild_fetched.name}')
    embed.add_field(name='Server ID:',value=f'{guild_fetched.id}')
    embed.add_field(name='Server region:',value=f'{guild_fetched.region}')
    embed.add_field(name='Server Creation Date:',value=f'{guild_fetched.created_at}')
    embed.add_field(name='Server Owner:',value=f'{guild_fetched.owner}')
    embed.add_field(name='Server Owner ID:',value=f'{guild_fetched.owner.id}')
    embed.add_field(name='Member Count:',value=f'{guild_fetched.member_count}')
    embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
    embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"milk") and not message.author.bot:
    embed = discord.Embed(title="You have summoned the milkman",color=random.randint(0, 16777215))
    embed.set_image(url="https://media.discordapp.net/attachments/700506169243861202/778118626350989312/pillow_imagedraw1.gif")
    embed.set_footer(text="his milk is delicious")
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"dice_roll20") and not message.author.bot:
    pfp=message.author.avatar_url
    type_dice = "d20"
    dice_gif = "https://media1.tenor.com/images/c05126b9ad27709b3930670b6ab4c070/tenor.gif"
    dice_roll20=random.randint(1,20)
    dice_roll20 = str(dice_roll20)
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    file = discord.File("images/dice.png",filename="dice.png")
    embed_message = discord.Embed(title=f" Rolled a {dice_roll20}", description=time_used, color=random.randint(0, 16777215))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="attachment://dice.png")
    embed_message.set_author(name=f"{type_dice} Rolled by {message.author}:",icon_url=(pfp))
    embed_message.set_image(url=dice_gif)
    await message.channel.send(embed=embed_message,file=file)
    return
  
  if message.content.startswith(discordprefix+"dice_roll6") and not message.author.bot:
    pfp=message.author.avatar_url
    type_dice = "d6"
    dice_gif = "https://media1.tenor.com/images/2fcf7e0bdb5ed04fcb5092cf2479907e/tenor.gif"
    dice_roll6=random.randint(1,6)
    dice_roll6 = str(dice_roll6)
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" Rolled a {dice_roll6}", description=time_used, color=random.randint(0, 16777215))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763974044734718002/dice.png")
    embed_message.set_author(name=f"{type_dice} Rolled by {message.author}:",icon_url=(pfp))
    embed_message.set_image(url=dice_gif)
    await message.channel.send(embed=embed_message)
    return
  
  if message.content.startswith(discordprefix+"dice_roll4") and not message.author.bot:
    pfp=message.author.avatar_url
    type_dice = "d4"
    dice_gif = "https://cdn.discordapp.com/emojis/626236311539286016.gif"
    dice_roll4=random.randint(1,4)
    dice_roll4 = str(dice_roll4)
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" Rolled a {dice_roll4}", description=time_used, color=random.randint(0, 16777215))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763974044734718002/dice.png")
    embed_message.set_author(name=f"{type_dice} Rolled by {message.author}:",icon_url=(pfp))
    embed_message.set_image(url=dice_gif)
    await message.channel.send(embed=embed_message)
    return

  if message.content.startswith(discordprefix+"dice_roll8") and not message.author.bot:
    pfp=message.author.avatar_url
    type_dice = "d8"
    dice_gif = "https://cdn.discordapp.com/emojis/626236311539286016.gif"
    dice_roll8=random.randint(1,8)
    dice_roll8 = str(dice_roll8)
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" Rolled a {dice_roll8}", description=time_used, color=random.randint(0, 16777215))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763974044734718002/dice.png")
    embed_message.set_author(name=f"{type_dice} Rolled by {message.author}:",icon_url=(pfp))
    embed_message.set_image(url=dice_gif)
    await message.channel.send(embed=embed_message)
    return

  if message.content.startswith(discordprefix+"dice_roll12") and not message.author.bot:
    pfp=message.author.avatar_url
    type_dice = "d12"
    dice_gif = "https://cdn.discordapp.com/emojis/626236311539286016.gif"
    dice_roll12=random.randint(1,12)
    dice_roll12 = str(dice_roll12)
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" Rolled a {dice_roll12}", description=time_used, color=random.randint(0, 16777215))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763974044734718002/dice.png")
    embed_message.set_author(name=f"{type_dice} Rolled by {message.author}:",icon_url=(pfp))
    embed_message.set_image(url=dice_gif)
    await message.channel.send(embed=embed_message)
    return

  if message.content.startswith(discordprefix+"dice_roll100") and not message.author.bot:
    pfp=message.author.avatar_url
    type_dice = "d100"
    dice_gif = "https://cdn.discordapp.com/emojis/626236311539286016.gif"
    dice_roll100=random.randint(1,100)
    dice_roll100 = str(dice_roll100)
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" Rolled a {dice_roll100}", description=time_used, color=random.randint(0, 16777215))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763974044734718002/dice.png")
    embed_message.set_author(name=f"{type_dice} Rolled by {message.author}:",icon_url=(pfp))
    embed_message.set_image(url=dice_gif)
    await message.channel.send(embed=embed_message)
    return

  if message.content.startswith(discordprefix+"dice_roll10") and not message.author.bot:
    pfp=message.author.avatar_url
    type_dice = "d10"
    dice_gif = "https://cdn.discordapp.com/emojis/626236311539286016.gif"
    dice_roll10=random.randint(1,10)
    dice_roll10 = str(dice_roll10)
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" Rolled a {dice_roll10}", description=time_used, color=random.randint(0, 16777215))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763974044734718002/dice.png")
    embed_message.set_author(name=f"{type_dice} Rolled by {message.author}:",icon_url=(pfp))
    embed_message.set_image(url=dice_gif)
    await message.channel.send(embed=embed_message)
    return

  if message.content.startswith(discordprefix+"cc_") and not message.author.bot:
    from PIL import Image
    import Pixman
    new_cmd = message.content.replace(discordprefix+"cc_","").split(" ")[0]
    
    
    mode =0
    if ('1' in new_cmd):
      mode=1
    if ('2' in new_cmd):
      mode=2
   
   
    if (new_cmd != new_cmd.replace("view","")):
      wire=mode
      if(wire<2):
        await color_code.veiw(message.author,message.channel,wire,0)
      else:
        _user = message.author
        _color_code = color_code.get(_user)
        decoder = Pixman.ram()
        image  = Pixman.get()
        image.decode(decoder.b(_color_code))
        image.render()
        image.export("render.png")
        await message.channel.send("Color Code of "+_user.name+"```"+_color_code+"```")
        await message.channel.send(file=discord.File('render.png'))
    
    if(new_cmd != new_cmd.replace("iv","")):
      #View
      if(mode<2):
        await color_code.veiw(message.author,message.channel,mode,1)
      else:
        _user = message.author
        _color_code = color_code.invert(color_code.get(_user))
        decoder = Pixman.ram()
        image  = Pixman.get()
        image.decode(decoder.b(_color_code))
        image.render()
        image.export("render.png")
        await message.channel.send("Color Code of "+_user.name+"```"+_color_code+"```")
        await message.channel.send(file=discord.File('render.png'))
    
    if (new_cmd != new_cmd.replace("test","")):
      instructs = message.content.replace("JDBot*cc_test ","")
      wire=mode
      print(wire)
      if(wire<2):
        #await color_code.veiw("NULL",message.channel,wire,0)
        if(instructs[0]=='8'):
          await color_code.veiw_raw(instructs,message.channel,wire)
        else:
          await color_code.veiw("NULL",message.channel,wire,0)
      else:
        _user = message.author 
        _color_code = color_code.get(_user)
        decoder = Pixman.ram()
        image  = Pixman.get()
        image.decode(decoder.b(_color_code))
        image.render()
        image.export("render.png")
        await message.channel.send("Color Code of "+_user.name+"```"+_color_code+"```")
        await message.channel.send(file=discord.File('render.png'))
      await message.delete()

      
    if(new_cmd != new_cmd.replace("save"," ")):
      #Save
      new_cmd=new_cmd.replace("save ","")
      if (new_cmd[0] != ' '):
        color_code.save(message.author,new_cmd)
        await message.delete()
        await message.channel.send("Color Code Saved!")
      else:
        print(new_cmd)
        await message.delete()
        await message.channel.send("Invalid Format!")

      

    if(new_cmd != new_cmd.replace("invert","")):
      #Invert
      if(color_code.valid_cc(message.author)):
        color_code.save(message.author,color_code.invert(color_code.get(message.author)))
        await message.channel.send("Color Code Inverted And Saved!")

    
    return

  if message.content.startswith(discordprefix+"file") and not message.author.bot:
    await message.channel.send(message.attachments)
    if message.attachments == []:
      await message.channel.send("\n No file submitted")
    if len(message.attachments) > 0:
      await message.channel.send("\n That's good")
    return
  
  if message.content.startswith(discordprefix+"nick") and  user.guild_permissions.manage_nicknames == True and not message.author.bot:
    nick_name=message.content.replace(discordprefix+"nick ","")
    if nick_name == "":
      nick_name = None
    guild_used=message.guild
    bot_permissions = message.guild.me
    if bot_permissions.guild_permissions.manage_nicknames == True:
      try: 
        await message.author.edit(nick=nick_name)
      except discord.errors.Forbidden:
        await message.channel.send("Try moving the bot's role over the user.")
    if bot_permissions.guild_permissions.manage_nicknames == False:
      await message.channel.send("sadly the bot doesn't have permissions")
    return

  if message.content.startswith(discordprefix+"user info") and not message.author.bot or message.content.startswith(discordprefix+"user_info") and not message.author.bot or message.content.startswith(discordprefix+"user-info") and not message.author.bot or message.content.startswith(discordprefix+"userinfo") and not message.author.bot:
    valid_command_test = message.content.replace(discordprefix,"")
    if(valid_command_test != valid_command_test.replace("user info","")):
      pass
    if(valid_command_test != valid_command_test.replace("user_info","")):
      pass
    if(valid_command_test != valid_command_test.replace("user-info","")):
      pass
    if(valid_command_test != valid_command_test.replace("userinfo","")):
      pass
    user99=await userinfo.user_grab(message)
    guild_used=message.guild
    user99_plus=guild_used.get_member(user99.id)
    avatar99 = user99.avatar_url
    bot_decide = user99.bot
    #if it's a bot(bool expression)
    if bot_decide == True:
      user_type = "Bot"
    if bot_decide==False:
      user_type = "User"
    #user_type will become useful later.
    user_id=str(user99.id)
    try:
      joined_guild = user99_plus.joined_at.strftime('%m/%d/%Y %H:%M:%S')
    except:
      joined_guild = "N/A"
    user_create = user99.created_at.strftime('%m/%d/%Y %H:%M:%S')
    try:
      user_status=str(user99_plus.status)
    except:
      user_status = "NULL"
    user_status = user_status.upper()
    try:
      nickname = str(user99_plus.nick)
    except:
      nickname = "None"
    x = 0
    try:
      while x < len(user99_plus.roles):
        x = x + 1
      highest_role=user99_plus.roles[x-1]
    except:
      highest_role = "N/A"
    guild_list = " "
    for guild in client.guilds:
      if user99 in guild.members:
        guild_list+=(", "+guild.name)
    if guild_list == " ":
      guild_list = "Null"
    #user_level = int(DatabaseConfig.db.users_testing.find_one({"user_id":user99.id})["level"])
    #user_local_rank = RankSystem.GetRank(user99,message.guild)
    #user_global_rank = RankSystem.GetRank(user99)
    embedVar = discord.Embed(title=str(user99),description=user_type, color=random.randint(0, 16777215))
    embedVar.set_image(url=avatar99)
    embedVar.add_field(name="Username: ", value = user99.name)
    embedVar.add_field(name="Discriminator:",value=user99.discriminator)
    embedVar.add_field(name="Nickname: ", value = nickname)
    embedVar.add_field(name="Joined Discord: ",value = user_create)
    embedVar.add_field(name="Joined Guild: ",value = joined_guild)
    embedVar.add_field(name="Part of Guilds:", value=guild_list)
    embedVar.add_field(name="ID:",value=user_id)
    embedVar.add_field(name="Status:",value=user_status)
    embedVar.add_field(name="Highest Role:",value=highest_role)
    #embedVar.add_field(name="Level: ",value = user_level)
    #embedVar.add_field(name="Global Rank: ",value=user_global_rank)
    #embedVar.add_field(name="Local Rank: ",value=user_local_rank)
    await message.channel.send(embed=embedVar)
    #try:
    print("USERNAME: "+user99.name)
    await RankSystem.GetStatus(message,user99)
   # except:
      #await message.channel.send("User not in Rank System")
    #turn these into embed info stuff. hash check will just an embed image(so feel free to delete hash_check i-tself, but keep avatar99, or at least the stuff to get it.)
    return
    #please make this into an embed


  if message.content.startswith(discordprefix+"tenor shuffle") and not message.author.bot:
    urls = []
    order_wanted = message.content.replace(discordprefix+"tenor shuffle","")
    apikey =  os.environ["tenor_key"]
    limit = 5
    url = f"https://api.tenor.com/v1/search?q={order_wanted}&key={apikey}&limit={limit}&contentfilter=medium"

    async with aiohttp.ClientSession() as cs:
      try:
        async with cs.get(url) as response:
          if response.status == 200:
            data_used= await response.json()
            for i in range(len(data_used['results'])):
              url = data_used['results'][i]['media'][0]['gif']['url']
              urls.append(url)
      except aiohttp.ClientConnectorError:
        await message.channel.send("Bot ran into an error please try again a bit later.\n Please DM the Bot owner about this")
        return
      
      value_grabber=random.randint(0,len(urls))
      order_image = urls[value_grabber]
      await message.delete()
      order_description = (f"{message.author} ordered a {order_wanted}")
      pfp = message.author.avatar_url
      order_time = (message.created_at).strftime('%m/%d/%Y %H:%M:%S')
      order_info = (f"order for {message.author}:")
      embed_info = discord.Embed(title=f"Item: {order_wanted}", description=order_description,  color=random.randint(0, 16777215))
      embed_info.set_footer(text = f"{message.author.id} \nTime: {order_time}")
      embed_info.set_author(name=order_info,icon_url=(pfp))
      embed_info.add_field(name="Powered by:",value="Tenor")
      embed_info.set_image(url=order_image)
      await message.channel.send(embed=embed_info)
      await client.get_channel(738912143679946783).send(embed=embed_info)
      image_channel = client.get_channel(764543893118648342)
      await image_channel.send("let's see the best result")
      for i in range(len(data_used['results'])):
        url = data_used['results'][i]['media'][0]['gif']['url']
        await image_channel.send(url)
      return
    
    if not response.status_code == 200:
      await message.channel.send("Failed searching for the gif")
    return

  if message.content.startswith(discordprefix+"tenor") and not message.author.bot:
    urls_dictionary = {}
    order_wanted = message.content.replace(discordprefix+"tenor","")
    apikey =  os.environ["tenor_key"]
    limit = 5
    url = f"https://api.tenor.com/v1/search?q={order_wanted}&key={apikey}&limit={limit}&contentfilter=medium"

    async with aiohttp.ClientSession() as cs:
      try:
        async with cs.get(url) as response:
          if response.status == 200:
            data_used= await response.json()
            for i in range(len(data_used['results'])):
              url = data_used['results'][i]['media'][0]['gif']['url']
              title = data_used['results'][i]["itemurl"]
              urls_dictionary[title]=url       
      except aiohttp.ClientConnectorError:
        await message.channel.send("Bot ran into an error please try again a bit later.\n Please DM the Bot owner about this")
        await message.channel.send("if you did this on purpose, just stop.")
        return

      gifNearest = sorted(urls_dictionary, key=lambda x: SequenceMatcher(None, x, order_wanted).ratio())[-1]
      order_image = urls_dictionary[gifNearest]
      await message.delete()
      order_description = (f"{message.author} ordered a {order_wanted}")
      pfp = message.author.avatar_url
      order_time = (message.created_at).strftime('%m/%d/%Y %H:%M:%S')
      order_info = (f"order for {message.author}:")
      embed_info = discord.Embed(title=f"Item: {order_wanted}", description=order_description,  color=random.randint(0, 16777215))
      embed_info.set_footer(text = f"{message.author.id} \nTime: {order_time}")
      embed_info.set_author(name=order_info,icon_url=(pfp))
      embed_info.add_field(name="Powered by:",value="Tenor")
      embed_info.set_image(url=order_image)
      await message.channel.send(embed=embed_info)
      await client.get_channel(738912143679946783).send(embed=embed_info)
      image_channel = client.get_channel(764543893118648342)
      await image_channel.send("let's see the best result")
      for i in range(len(data_used['results'])):
        url = data_used['results'][i]['media'][0]['gif']['url']
        await image_channel.send(url)
      return
    
    if not response.status_code == 200:
      await message.channel.send("Failed searching for the gif")
    return  

  if message.content.startswith(discordprefix+"giphy shuffle") and not message.author.bot:
    order_wanted = message.content.replace(discordprefix+"giphy shuffle","")
    import giphy_client
    from giphy_client.rest import ApiException
    giphy_usage = giphy_client.DefaultApi()
    try:
      api_response = giphy_usage.gifs_search_get(api_key=os.environ["giphy_token"],limit=5,rating="g",q=order_wanted)
      lst = list(api_response.data)
      if len(lst) > 0:
        gif_number = random.randint(0,len(lst))
        gifNearest = lst[gif_number]
        order_image = (f"https://media3.giphy.com/media/{gifNearest.id}/giphy.gif")
        await message.delete()
        order_description = (f"{message.author} ordered a {order_wanted}")
        pfp = message.author.avatar_url
        order_time = (message.created_at).strftime('%m/%d/%Y %H:%M:%S')
        order_info = (f"order for {message.author}:")
        embed_info = discord.Embed(title=f"Item: {order_wanted}", description=order_description,  color=random.randint(0, 16777215))
        embed_info.set_footer(text = f"{message.author.id} \nTime: {order_time}")
        embed_info.set_author(name=order_info,icon_url=(pfp))
        embed_info.add_field(name="Powered by:",value="GIPHY")
        embed_info.set_image(url=order_image)
        await message.channel.send(embed=embed_info)
        await client.get_channel(738912143679946783).send(embed=embed_info)
        image_channel = client.get_channel(764543893118648342)
        await image_channel.send("let's see the best result")
        for x in lst:
          await image_channel.send(x.url)
      
      if len(lst) == 0:
        await message.channel.send("search failed... \n Error: No gifs found.")

    except ApiException as e:
      await message.channel.send("Either the rate limit was reached or you didn't insert anything")
      print(e)

    return

  if message.content.startswith(discordprefix+"giphy") and not message.author.bot:
    order_wanted = message.content.replace(discordprefix+"giphy ","")
    import giphy_client
    from giphy_client.rest import ApiException
    giphy_usage = giphy_client.DefaultApi()
    try:
      api_response = giphy_usage.gifs_search_get(api_key=os.environ["giphy_token"],limit=5,rating="g",q=order_wanted)
      lst = list(api_response.data)
      if len(lst) > 0:
        gifNearest = sorted(lst, key=lambda x: SequenceMatcher(None, x.url, order_wanted).ratio())[-1]
        order_image = (f"https://media3.giphy.com/media/{gifNearest.id}/giphy.gif")
        await message.delete()
        order_description = (f"{message.author} ordered a {order_wanted}")
        pfp = message.author.avatar_url
        order_time = (message.created_at).strftime('%m/%d/%Y %H:%M:%S')
        order_info = (f"order for {message.author}:")
        embed_info = discord.Embed(title=f"Item: {order_wanted}", description=order_description,  color=random.randint(0, 16777215))
        embed_info.set_footer(text = f"{message.author.id} \nTime: {order_time}")
        embed_info.set_author(name=order_info,icon_url=(pfp))
        embed_info.add_field(name="Powered by:",value="GIPHY")
        embed_info.set_image(url=order_image)
        await message.channel.send(embed=embed_info)
        await client.get_channel(738912143679946783).send(embed=embed_info)
        image_channel = client.get_channel(764543893118648342)
        await image_channel.send("let's see the best result")
        for x in lst:
          await image_channel.send(x.url)

      if len(lst) == 0:
        await message.channel.send("search failed... \n Error: No gifs found.")

    except ApiException as e:
      await message.channel.send("Either the rate limit was reached or you didn't insert anything")
      print(e)

    return

  if message.content.startswith(discordprefix+"order_shuffle") and not message.author.bot:
    from google_images_search import GoogleImagesSearch
    import time
    order_wanted = message.content.replace(discordprefix+"order_shuffle ","")
    time_before=time.process_time() 
    def my_progressbar(url, progress):
      url_collection.append(url)
    gis = GoogleImagesSearch(os.environ['image_api_key'],os.environ['google_image_key'], validate_images=False,progressbar_fn=my_progressbar)
    safe_search = {
      'q': order_wanted,
      'num': 5,
     'rights': 'cc_publicdomain',
     'fileType': 'jpg|gif|png|jpeg',
     'safe': 'medium',
     }
     
    try:
      gis.search(search_params = safe_search)
    except:
      await message.channel.send("Please wait for a while so the api key gets regenerated")
    for image_check in gis.results():
      try:
        raw_image_data = image_check.get_raw_data()
        discord.utils._get_mime_type_for_image(raw_image_data)
      except:
        gis.results().remove(image_check)
    
    for x in url_collection:
      async with aiohttp.ClientSession() as cs:
         async with cs.get(x) as response:
            try:
              img = discord.utils._get_mime_type_for_image(await response.read())
            except:
              url_collection.remove(x)
              print(x)
    
    await message.delete()

    order_description = (f"{message.author} ordered a {order_wanted}")
    pfp = message.author.avatar_url
    order_time = (message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    order_info = (f"order for {message.author}:")

    embed_info = discord.Embed(title=f"Item: {order_wanted}", description=order_description,  color=random.randint(0, 16777215))

    embed_info.set_footer(text = f"{message.author.id} \nTime: {order_time} \nCopyright: Public Domain")
    embed_info.set_author(name=order_info,icon_url=(pfp))

    time_after=time.process_time()
    time_spent = int((time_after - time_before)*1000)
    embed_info.add_field(name="Time Spent:",value=f"{time_spent} MS")  
    image_channel = client.get_channel(764543893118648342)

    if len(url_collection) > 0:
      embed_info.add_field(name="Powered by:",value="Google Images Api")
      max_number=len(url_collection)
      spinner=random.randint(0,max_number-1)

      emoji_image = url_collection[spinner]

      await image_channel.send("let's see the best result")

      for x in url_collection:

        await image_channel.send(x)

    if len(url_collection) == 0:

      embed_info.add_field(name="Powered by:",value="Emojis")

      emojiNearest = sorted(client.emojis, key=lambda x: SequenceMatcher(None, x.name, order_wanted).ratio())[-1] 

      emoji_image=emojiNearest.url 

    embed_info.set_image(url=emoji_image)

    await message.channel.send(embed=embed_info)

    await client.get_channel(738912143679946783).send(embed=embed_info)

    url_collection = []
    return

  if message.content.startswith(discordprefix+"image_check") and not message.author.bot:
    check_image = message.content.replace(discordprefix+"image_check ","")
    async with aiohttp.ClientSession() as cs:
      try:
        async with cs.get(check_image) as response:
          valid_image = await response.read()
      except aiohttp.ClientConnectorError:
        await message.channel.send("Not a valid url")
        return
      except aiohttp.InvalidURL:
        await message.channel.send("seriously a fake url?")
        return
    try:
      valid_image=discord.utils._get_mime_type_for_image(valid_image)
      await message.channel.send(valid_image)
    except discord.errors.InvalidArgument:
      await message.channel.send("Not a valid image")
    return

  if message.content.startswith(discordprefix+"order") and not message.author.bot:
    import time
    from google_images_search import GoogleImagesSearch
    order_wanted = message.content.replace(discordprefix+"order ","")
    time_before=time.process_time() 
    def my_progressbar(url, progress):
      url_collection.append(url)
    gis = GoogleImagesSearch(os.environ['image_api_key'],os.environ['google_image_key'], validate_images=False,progressbar_fn=my_progressbar)
    safe_search = {
      'q': order_wanted,
      'num': 5,
     'rights': 'cc_publicdomain',
     'fileType': 'jpg|gif|png|jpeg',
     'safe': 'medium',
     }

    try:

      gis.search(search_params = safe_search)
    except:

      await message.channel.send("Please wait for a while so the api key gets regenerated")

    my_bytes_io = BytesIO()

    for image_check in gis.results():
      my_bytes_io.seek(0)
      try:
        raw_image_data = image_check.get_raw_data()
        image_check.copy_to(my_bytes_io, raw_image_data)
        temp_img = discord.utils._get_mime_type_for_image(my_bytes_io)

      except:
        gis.results().remove(image_check)

    for x in url_collection:
      async with aiohttp.ClientSession() as cs:
        async with cs.get(x) as response:
          try:
            img = discord.utils._get_mime_type_for_image(await response.read())
          except:
            url_collection.remove(x)

    time_after=time.process_time()
    time_spent = int((time_after - time_before)*1000)
    await message.delete()
    order_description = (f"{message.author} ordered a {order_wanted}")
    pfp = message.author.avatar_url
    order_time = (message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    order_info = (f"order for {message.author}:")
    embed_info = discord.Embed(title=f"Item: {order_wanted}", description=order_description,  color=random.randint(0, 16777215))
    embed_info.set_footer(text = f"{message.author.id} \nTime: {order_time} \nCopyright: Public Domain")
    embed_info.add_field(name="Time Spent:",value=f"{time_spent} MS")
    embed_info.set_author(name=order_info,icon_url=(pfp))
    image_channel = client.get_channel(764543893118648342)
    if len(url_collection) > 0:

      embed_info.add_field(name="Powered by:",value="Google Images Api")

      emoji_image = sorted(url_collection, key=lambda x: SequenceMatcher(None, x, order_wanted).ratio())[-1]

      await image_channel.send("let's see the best result")

      for x in url_collection:

        await image_channel.send(x)

    if len(url_collection) == 0:

      embed_info.add_field(name="Powered by:",value="Emojis")

      emojiNearest = sorted(client.emojis, key=lambda x: SequenceMatcher(None, x.name, order_wanted).ratio())[-1] 

      emoji_image=emojiNearest.url 

    embed_info.set_image(url=emoji_image)

    await message.channel.send(embed=embed_info)

    await client.get_channel(738912143679946783).send(embed=embed_info)

    url_collection = []

    return

  if message.content.startswith(discordprefix+"exportPfp") and message.author.id in admins and not message.author.bot:
    GetPfp.DownloadAllPfp(message)
    return

  if message.content.startswith(discordprefix+"fetch_content") and not message.author.bot:
    data_here=message.content.replace(discordprefix+"fetch_content ","")
    if data_here == discordprefix+"fetch_content":
      await message.channel.send("please send actual text")
      return
    data_here=discord.utils.escape_mentions(data_here)
    data_here=discord.utils.escape_markdown(data_here,as_needed=False,ignore_links=False)
    for x in message.channel_mentions:
      data_here = data_here.replace(x.mention,f"\{x.mention}")
    emojis_return = emojis.get(data_here)
    for x in emojis_return:
      data_here = data_here.replace(x,f"\{x}")
    await message.channel.send(f"{data_here}")
    return

  if message.content.startswith(discordprefix+"random_history") and not message.author.bot:
    amount = message.content.replace(discordprefix+"random_history","")
    try:
      amount = int(amount)
      if amount > 1 and amount < 51:
        url=f"https://history.geist.ga/api/many?amount={amount}"
      if amount > 50 or amount < 2:
        url = "https://history.geist.ga/api/one"
    except ValueError:
      url = "https://history.geist.ga/api/one"
    async with aiohttp.ClientSession() as cs:
      async with cs.get(url) as r:
        history = await r.json()
    for x in history:
      results=history[x]
    if type(results) is list:
      for x in results:
        await message.channel.send(f":earth_africa: {x}")
    if type(results) is str:
      await message.channel.send(f":earth_africa: {results}")
    return

  if message.content.startswith(discordprefix+"guild_get") and not message.author.bot:
      if message.guild != None:
        await message.channel.send(message.guild.id)
      if message.guild == None:
          await message.channel.send("This doesn't work in Dms.")
      return
  
  if message.content.startswith(discordprefix+"guild_info") and not message.author.bot:
      server = message.content.replace(discordprefix+"guild_info","")
      try:
          server = int(server)
      except:
          server = message.guild.id
      server = client.get_guild(server)
      if server != None:
        bots = 0
        real_members = 0
        for x in server.members:
          if x.bot == True:
              bots=bots + 1
          if x.bot == False:
              real_members = real_members + 1
        emojis_static = 0
        emojis_animated = 0
        for x in server.emojis:
            if x.animated == False:
                emojis_static = emojis_static + 1
            if x.animated == True:
                emojis_animated = emojis_animated + 1
        embed = discord.Embed(title="Guild Info:",color=random.randint(0, 16777215))
        embed.add_field(name="Server Name:",value=server.name)
        embed.add_field(name="Server ID:",value=server.id)
        embed.add_field(name="Server region",value=server.region)
        embed.add_field(name="Server created at:",value=f"{server.created_at} UTC")
        embed.add_field(name="Server Owner:",value=server.owner)
        embed.add_field(name="Member Count:",value=server.member_count)
        embed.add_field(name="Users:",value=real_members)
        embed.add_field(name="Bots:",value=bots)
        embed.add_field(name="Channel Count:",value=len(server.channels))
        embed.add_field(name="Role Count:",value=len(server.roles))
        embed.set_thumbnail(url=str(server.icon_url))
        embed.add_field(name="Emoji Limit:",value=server.emoji_limit)
        embed.add_field(name="Max File Size:",value=f"{server.filesize_limit/1000000} MB")
        embed.add_field(name="Shard ID:",value=server.shard_id)
        embed.add_field(name="Animated Icon",value=server.is_icon_animated())
        embed.add_field(name="Static Emojis",value=emojis_static)
        embed.add_field(name="Animated Emojis",value=emojis_animated)
        embed.add_field(name="Total Emojis:",value=f"{len(server.emojis)}/{server.emoji_limit*2}")
        await message.channel.send(embed=embed)
      if server == None:
          await message.channel.send("Bot can't see this guild.")
      return
  if message.content.startswith(discordprefix+"server_info") and not message.author.bot:
      server = message.content.replace(discordprefix+"server_info","")
      try:
          server = int(server)
      except:
          server = message.guild.id
      server = client.get_guild(server)
      if server != None:
        bots = 0
        real_members = 0
        for x in server.members:
          if x.bot == True:
              bots=bots + 1
          if x.bot == False:
              real_members = real_members + 1
        emojis_static = 0
        emojis_animated = 0
        for x in server.emojis:
            if x.animated == False:
                emojis_static = emojis_static + 1
            if x.animated == True:
                emojis_animated = emojis_animated + 1
        embed = discord.Embed(title="Guild Info:",color=random.randint(0, 16777215))
        embed.add_field(name="Server Name:",value=server.name)
        embed.add_field(name="Server ID:",value=server.id)
        embed.add_field(name="Server region",value=server.region)
        embed.add_field(name="Server created at:",value=f"{server.created_at} UTC")
        embed.add_field(name="Server Owner:",value=server.owner)
        embed.add_field(name="Member Count:",value=server.member_count)
        embed.add_field(name="Users:",value=real_members)
        embed.add_field(name="Bots:",value=bots)
        embed.add_field(name="Channel Count:",value=len(server.channels))
        embed.add_field(name="Role Count:",value=len(server.roles))
        embed.set_thumbnail(url=str(server.icon_url))
        embed.add_field(name="Emoji Limit:",value=server.emoji_limit)
        embed.add_field(name="Max File Size:",value=f"{server.filesize_limit/1000000} MB")
        embed.add_field(name="Shard ID:",value=server.shard_id)
        embed.add_field(name="Animated Icon",value=server.is_icon_animated())
        embed.add_field(name="Static Emojis",value=emojis_static)
        embed.add_field(name="Animated Emojis",value=emojis_animated)
        embed.add_field(name="Total Emojis:",value=f"{len(server.emojis)}/{server.emoji_limit*2}")
        await message.channel.send(embed=embed)
      if server == None:
          await message.channel.send("Bot can't see this guild.")
      return

  if message.content.startswith(discordprefix+"server_icon") and not message.author.bot:
    await message.channel.send(GetPfp.GetServerPfp(message))
    return

  if message.content.startswith(discordprefix+"pfp") and not message.author.bot:
    await message.channel.send((await GetPfp.GetUserPfp(message)).avatar_url)
    return

  if message.content.startswith(discordprefix+"avatar") and not message.author.bot:
    user = await GetPfp.GetUserPfp(message)
    pfp = user.avatar_url
    embed = discord.Embed(title = f"{user.name}'s avatar:",color=random.randint(0, 16777215))
    embed.set_image(url=(pfp))
    await message.channel.send(embed=embed)
    
    return

  if message.content.startswith(discordprefix+"advice") and not message.author.bot:

    advice_response=random.choice(random_response.advice)
    embed = discord.Embed(title = "Here is some advice for you!",color=random.randint(0, 16777215))
    embed.add_field(name = f"{advice_response}", value = "Hopefully this helped!")
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"leave guild") and message.author.id in admins and not message.author.bot:
    guild_info = client.get_guild(int(message.content.split(" ")[2]))

    await guild_info.leave()

    return

  if message.content.startswith(discordprefix+"status") and message.author.id in admins and not message.author.bot:
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(message.content.replace(discordprefix+"status ","")))
    return


  if message.content.startswith(discordprefix+"random_number") and not message.author.bot:
    try:
      number_one = int(message.content.split(" ")[1])
      number_two =  int(message.content.split(" ")[2])
    except:
      await message.channel.send("That is not a number! I shall default to numbers between 0 to 100")
      number_one = 0
      number_two = 100


    if number_one > number_two:
      await message.channel.send("Smaller number first")
    
    random_number = random.randint(number_one, number_two)

    embed = discord.Embed(title = f"A random number from {number_one} to {number_two}:", description = f"{random_number}",color=random.randint(0, 16777215))
    await message.channel.send(embed = embed)
    
    return

  if message.content.startswith(discordprefix+"about") and not message.author.bot:
    embed_message = discord.Embed(title="About(commands):", description=all_commands, color=random.randint(0, 16777215))

    user_send2 = message.author
    if (user_send2.dm_channel is None):
      await user_send2.create_dm()

    await user_send2.send(embed=embed_message)

    embed_message2 = discord.Embed(title="About(credits):", description=credits, color=random.randint(0, 16777215))
    await user_send2.send(embed=embed_message2)

    helpmsg2 = "prefix is JDBot*, More commands are:\n "+all_commands2

    embed_message = discord.Embed(title="About(commands):",description=helpmsg2, color=random.randint(0, 16777215))

    await message.author.dm_channel.send(embed=embed_message)

    embed_message = discord.Embed(title="About(legal):",description=legal_info, color=random.randint(0, 16777215))

    await message.author.dm_channel.send(embed=embed_message)

    return

  if message.content.startswith(discordprefix+"time") and not message.author.bot:

    currenttime = datetime.datetime.now(timezone(time_location)).strftime("%m/%d/%Y, %H:%M:%S")

    embed = discord.Embed(title="Current Server Time:",description=currenttime,color=random.randint(0, 16777215))
    embed.add_field(name="Time Zone(closest):",value=time_location)
    await message.channel.send(embed=embed)

    return
    
  if message.content.startswith(discordprefix+"say") and not message.author.bot:
    current_message = message.content.replace(discordprefix+"say","")
    if current_message == "":
      return
    current_message = current_message.lstrip()
    if len(message.channel_mentions) > 0:
      target=message.channel_mentions[0]
      if current_message.startswith(target.mention):
        await message.delete()
        current_message = current_message.replace(target.mention," ")
        try:
          await target.send(current_message)
        except:
          await message.channel.send(current_message)
      elif not current_message.startswith(target.mention):
        await message.delete()
        await message.channel.send(current_message)
    if len(message.channel_mentions) == 0:
      await message.delete()
      await message.channel.send(current_message)
    return

  if message.content.startswith(discordprefix+"support DM ") and not message.author.bot:

    support_msg = message.content.replace(discordprefix+"support DM ","")

    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')

    pfp = message.author.avatar_url

    embed_message = discord.Embed(title=support_msg, description=time_used, color=random.randint(0, 16777215))

    embed_message.set_author(name=f"Help Needed from {message.author}:",icon_url=(pfp))

    embed_message.set_footer(text = f"{message.author.id} \nSupport Mode: DM")

    embed_message.set_thumbnail(url="https://cdn.discordapp.com/attachments/738912143679946783/763925088378552320/raise_hand.png")

    for ad_id in admin_contact:

      try:

        admin_user = client.get_user(ad_id)

        if (admin_user.dm_channel is None):
          await admin_user.create_dm()

        embed_message.add_field(name="Sent To:",value=str(admin_user))

      except:

        await message.channel.send(f'Error processesing user: {ad_id}')

    for adID in admin_contact:
      try:
        admin_user = client.get_user(adID)

        if (admin_user.dm_channel is None):
          await admin_user.create_dm()



        await admin_user.send(embed=embed_message)
      except:
        await message.channel.send(f'Error processesing user: {ad_id}')

      channel_used = client.get_channel(738912143679946783)
      await channel_used.send(embed=embed_message)
      return

  if message.content.startswith(discordprefix+"invert") and not message.author.bot:
    from PIL import Image
    import inverter
    if len(message.attachments) == 0:
      for message_wanted in await message.channel.history(limit=100).flatten():
        if not message_wanted.author.bot and len(message_wanted.attachments) != 0:
          image_invert =  message_wanted.attachments[0]
    if len(message.attachments) > 0:
      image_invert = message.attachments[0]
    img = await image_invert.read()
    try:
      img=Image.open(BytesIO(img))
    except:
      await message.channel.send("not a valid image.")
      return
    inverted_image = inverter.invert(img)
    buffer = BytesIO()
    image_format = (img.format)
    if img.format != "GIF":
      inverted_image.save(buffer,format = image_format)
    elif img.is_animated == False:
      inverted_image.save(buffer,format = image_format)
    elif img.is_animated == True:
      inverted_image.save(buffer,format = image_format,save_all=True)
    buffer.seek(0)
    file_name = (f"invert.{image_format}")
    file=discord.File(buffer, filename=file_name)
    embed = discord.Embed(title="Inverted image:",timestamp=(message.created_at),color=random.randint(0, 16777215))
    embed.set_image(url=f"attachment://invert.{image_format}")
    await message.channel.send(embed=embed,file=file)
    return


  if message.content.startswith(discordprefix+"closest_embed") and not message.author.bot:
    for message_wanted in await message.channel.history(limit=100).flatten():
      if len(message_wanted.embeds) != 0:
        for embed in message_wanted.embeds:
          await message.channel.send(embed=embed)
        return
    await message.channel.send("couldn't find any embeds")
    return

  if message.content.startswith(discordprefix+"emoji_check") and not message.author.bot:
    from PIL import Image
    obj = client.get_emoji(749442292045185084)
    img = await obj.url.read()
    check_time=Image.open(BytesIO(img))
    image_format=str(check_time.format).lower()
    width, height=(check_time.size)
    image_mode = (check_time.mode)
    byte_size = (len(img)/1000)
    size_used=(f"{byte_size} KB")
    divide_rate = (byte_size/256)
    new_width = int(width/divide_rate)
    new_height = int(height/divide_rate)
    dimensions=(new_width,new_height)
    file_name = (f"{obj.name}.{image_format}")
    check_time.resize(dimensions)
    buffer = BytesIO()
    check_time.save(buffer,format = image_format,save_all=True)
    buffer.seek(0)
    file=discord.File(buffer, filename=file_name)
    embed_message=discord.Embed(title=f"Emoji name : {obj.name}",timestamp=(message.created_at),color=random.randint(0, 16777215))
    embed_message.set_author(name=f"{message.author}",icon_url=(message.author.avatar_url))
    embed_message.add_field(name="Byte Size:",value=size_used)
    embed_message.add_field(name="PIL Image mode:",value=f"{image_mode}")
    embed_message.add_field(name="Width:",value=width)
    embed_message.add_field(name="Height:",value=height)
    embed_message.add_field(name="Image type:",value=image_format)
    embed_message.add_field(name="New Width:",value=new_width)
    embed_message.add_field(name="New Height:",value=new_height)
    #embed_message.add_field(name="New Byte Size:",value=f"{new_bytes} KB")
    embed_message.set_image(url=f"attachment://{file_name}")
    embed_message.set_thumbnail(url=obj.url)
    embed_message.set_footer(text = f"{message.author.id}")
    await message.channel.send(embed=embed_message,file=file)
    guild_1 = client.get_guild(748753645138608239)
    #await guild_1.create_custom_emoji(name = str(obj.name),image=emoji_bytes)
    return

  if message.content.startswith(discordprefix+"backup_emojis") and message.author.id in admins  and not message.author.bot:
    guild_search = client.get_guild(736422329399246990)
    guild_1 = client.get_guild(748753645138608239)
    guild_2 = client.get_guild(748753770476732499)
    guild_emoji_fetch = guild_search.emojis
    i = -1
    for obj in guild_emoji_fetch:
      img = await obj.url.read()
      if (len(img)/1000) > 255:
        await message.channel.send("too large")
        return
      if(i<50):
        if obj.animated == True:
          await guild_1.create_custom_emoji(name = str(obj.name),image=img)
        if obj.animated == False:
          i = i-1
      if(i>=50):
        if obj.animated == False:
          await guild_2.create_custom_emoji(name = str(obj.name),image=img)
        if str(obj.animated) == True:
          i =  i-1
    return

  if message.content.startswith(discordprefix+"delete_emojis") and message.author.id in admins and not message.author.bot:
    guild_1 = client.get_guild(748753645138608239)
    guild_2 = client.get_guild(748753770476732499)
    for x in guild_1.emojis:
      await x.delete()
    for y in guild_2.emojis:
      await y.delete()

    return

  if message.content.startswith(discordprefix+"emoji_clean") and message.author.id in admins and not message.author.bot:

    id_used = (763857844440268842)

    dump_server = client.get_guild(id_used)

    for x in dump_server.emojis:

      await x.delete()

    return

  if message.content.startswith(discordprefix+"emoji_add") and not message.author.bot and user.guild_permissions.manage_emojis == True:
    emote_collect = []
    from PIL import Image
    id_used = (message.guild.id)
    dump_server = client.get_guild(id_used)
    animated_amount = 0
    static_amount = 0

    for e in dump_server.emojis:
      if e.animated == "yes":
        animated_amount = animated_amount + 1
      if e.animated == "no":
        static_amount = static_amount + 1

    emoji_url = []
    emoji_name = []

    for em in (await emote.get(message)):
      emoji_url.append(em)

    for name in await emote.get2(message):
      emoji_name.append(name)
    e = 0

    while e < len(emoji_name):
      img_link = emoji_url[e]
      emoji_name_grabbed = emoji_name[e]
      try:
        async with aiohttp.ClientSession() as cs:
          async with cs.get(img_link) as response:
            img = Image.open(await response.read())
      except:
        await message.channel.send("Don't use emojis with webhooks or bots.")
        return

      if img.is_animated == True:
        if animated_amount < 50:
          pass_value = "yes"
          image = await response.read()
          emote_data = await dump_server.create_custom_emoji(name = emoji_name_grabbed,image=image)
          emote_collect.append(emote_data)
          animated_amount = animated_amount + 1

        if animated_amount >=50:

          pass_value = "no"

          await message.channel.send("That's why too many emojis")
      
      if img.is_animated == False:
        if static_amount < 50:
          image = await response.read()
          emote_data = await dump_server.create_custom_emoji(name = emoji_name_grabbed,image=image)
          emote_collect.append(emote_data)
          pass_value = "yes"
          static_amount = static_amount+1
        if static_amount >=50:
          pass_value = "no"

          await message.channel.send("That's why too many emojis") 

      e = e + 1

    e = 0

    pfp = client.user.avatar_url

    if emote_data.animated == True:

      animated_value = "Animated"

    if emote_data.animated == False:

      animated_value = "Static"

    if pass_value == "yes":

      for emote_data in emote_collect:
        time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
        emoji_embed=discord.Embed(title=f"Added Emote: {emote_data.name}",description=time_used,color=random.randint(0, 16777215))
        emoji_embed.set_author(name=f"{message.author} Added an emoji.",icon_url=(pfp))
        emoji_embed.add_field(name=f"Emoji Type:",value=f"{animated_value}")
        emoji_embed.set_image(url=emote_data.url)
        emoji_embed.set_footer(text = f"{message.author.id}\n Emoji in {dump_server.name}\n ID: {dump_server.id}")
        channel_used=client.get_channel(738912143679946783)
        await channel_used.send(embed=emoji_embed)
        await message.channel.send(embed=emoji_embed)
    return

  if message.content.startswith(discordprefix+"emoji_save") and not message.author.bot:
    emote_collect = []
    from PIL import Image
    id_used = (763857844440268842)
    dump_server = client.get_guild(id_used)
    animated_amount = 0
    static_amount = 0
    for e in dump_server.emojis:

      if e.animated == "yes":

        animated_amount = animated_amount + 1

      if e.animated == "no":

        static_amount = static_amount + 1

    emoji_url = []

    emoji_name = []

    for em in (await emote.get(message)):

      emoji_url.append(em)

    for name in emote.get2(message):

      emoji_name.append(name)

    e = 0

    while e < len(emoji_name):

      img_link = emoji_url[e]

      emoji_name_grabbed = emoji_name[e]

      async with aiohttp.ClientSession() as cs:
        async with cs.get(img_link) as response:
          img = Image.open(await response.read())

      if img.is_animated == True:

        if animated_amount < 50:

          pass_value = "yes"
          emote_data = await dump_server.create_custom_emoji(name = emoji_name_grabbed,image=await response.read())

          emote_collect.append(emote_data)

          animated_amount = animated_amount + 1

        if animated_amount >=50:

          pass_value = "no"

          await message.channel.send("That's why too many emojis")
      
      if img.is_animated == False:

        if static_amount < 50:

          emote_data = await dump_server.create_custom_emoji(name = emoji_name_grabbed,image=await response.read())

          emote_collect.append(emote_data)

          pass_value = "yes"

          static_amount = static_amount+1
        
        if static_amount >=50:

          pass_value = "no"

          await message.channel.send("That's why too many emojis") 

      e = e + 1

    e = 0

    pfp = client.user.avatar_url

    if emote_data.animated == True:

      animated_value = "Animated"

    if emote_data.animated == False:

      animated_value = "Static"

    if pass_value == "yes":

      for emote_data in emote_collect:

        time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')

        emoji_embed=discord.Embed(title=f"Added Emote: {emote_data.name}",description=time_used,color=random.randint(0, 16777215))

        emoji_embed.set_author(name=f"{message.author} Added an emoji.",icon_url=(pfp))

        emoji_embed.add_field(name=f"Emoji Type:",value=f"{animated_value}")

        emoji_embed.set_image(url=emote_data.url)

        emoji_embed.set_footer(text = f"{message.author.id}\n Emoji in {dump_server.name}\n ID: {dump_server.id}")

        channel_used=client.get_channel(738912143679946783)
        await channel_used.send(embed=emoji_embed)

        await message.channel.send(embed=emoji_embed)
    retur
  
  if message.content.startswith(discordprefix+"emoji_id") and not message.author.bot:
    emoji_id=message.content.replace(discordprefix+"emoji_id ","")
    try:
      int(emoji_id)
    except:
      await message.channel.send("make sure you pass actual emoji ids and not text.")
      return
    url_speacil=await emote.get_emoji_id(emoji_id)
    for url in url_speacil:
      embed = discord.Embed(description=f" Emoji ID: {emoji_id}",color=random.randint(0, 16777215))
      embed.set_image(url=url)
      await message.channel.send(embed=embed)
    return
  
  if message.content.startswith(discordprefix+"emoji") and not message.author.bot:
    for em in (await emote.get(message)):
      for name in emote.get2(message):
        embed=discord.Embed(title=f"Emoji: **{name}**",color=random.randint(0, 16777215))
        embed.set_image(url=em)
        await message.channel.send(embed=embed)
    await emote.default_emojis(message)
    return

  if message.content.startswith(discordprefix+"log off") and message.author.id in admins and not message.author.bot:
    await message.channel.send("Shutting off")
    await client.logout()
    return

  if message.content.startswith(discordprefix+"voice_create") and not message.author.bot and user.guild_permissions.manage_channels == True:
    link_data="https://discordapp.com/"+str(message.guild.id)
    try:
      channel_name = message.content.split(" ")[1]
    except:
      await message.channel.send("That's not a valid function")
      return
    voice_channel=await message.guild.create_voice_channel(channel_name)
    link_data = link_data+str(voice_channel.id)
    data_send = "The channel link exists at: "+str(link_data)
    await message.channel.send(data_send)
    return

  if message.content.startswith(discordprefix+"channel_create") and not message.author.bot and user.guild_permissions.manage_channels == True:
    try:
      channel_name = message.content.split(" ")[1]
    except:
      await message.channel.send("That's not a valid function")
      return

    channel_info = await message.guild.create_text_channel(channel_name)
    channel_mention=channel_info.mention
    channel_name = channel_info.name
    typical_message = "the channel "+str(channel_name)+" has just been created, link to it is here: "+str(channel_mention)
    await message.channel.send(typical_message)
    await message.delete()
    return
  
  if message.content.startswith(discordprefix+"webhook_create") and not message.author.bot and user.guild_permissions.manage_webhooks == True:
    valid_image = ["PNG",".GIF",".JPG","JPEG"]
    from PIL import Image
    try:
      webhook_name = message.content.split(" ")[1]
    except:
      webhook_name = "Webhook"
    try:
      content_message = message.content.split(" ")[2]
    except:
      content_message = "test"

    if content_message == "" or content_message == " ":
      content_message = "test"
    await message.channel.send("Making Webhooks with your manage permissions(safety reasons)")

    if len(message.attachments) > 0:
      image_used = message.attachments[0]

      async with aiohttp.ClientSession() as cs:
        try:
          async with cs.get(image_used.url) as response:
            img = Image.open(await response.read())
        except aiohttp.ClientConnectorError:
          await message.channel.send("somehow you got pass the system") 

        except aiohttp.InvalidURL:
          await message.channel.send("seriously a fake url?")
          return

      if (img.format).upper() in valid_image:
        webhook=await message.channel.create_webhook(name=webhook_name,reason=content_message,avatar=await response.read())
      if not (img.format).upper() in valid_image:
        await message.channel.send("Not in the right format, defaulting to no avatar")
        webhook=await message.channel.create_webhook(name=webhook_name,reason=content_message)
    if message.attachments == []:
      webhook=await message.channel.create_webhook(name=webhook_name,reason=content_message)
    if (message.author.dm_channel is None):
      await message.author.create_dm()
    await message.delete()

    await message.author.dm_channel.send("The link to use a webhook url is coming right now.")
    await message.author.dm_channel.send(webhook.url)
    await message.channel.send(f"Now testing... with {content_message}")
    webhook_url = webhook.url
    webhook = discord_webhook.DiscordWebhook(url=webhook_url)
    embed = discord_webhook.DiscordEmbed(title=f"{message.author}'s Message:",color=random.randint(0, 16777215))
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed.add_embed_field(name=content_message, value=time_used)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    return

  if message.content.startswith(discordprefix+"webhook_delete") and not message.author.bot:
    url_used=message.content.split(" ")[1]
    await message.delete()
    async with aiohttp.ClientSession() as cs:
      try:
        async with cs.get(url_used) as response:
          if response.status != 200:
            await message.channel.send("Not a valid link")
          if response.status == 200:
            json_data= await response.json()
            used_id = int(json_data["id"])
            guild_id = int(json_data["guild_id"])
            guild_used = client.get_guild(guild_id)
            permission_check=guild_used.get_member(user.id)
            webhook_name=json_data["name"]
            check_bool=permission_check.guild_permissions.manage_webhooks
            if check_bool == True:
              webhook_used=await client.fetch_webhook(used_id)
              await webhook_used.delete()
              full_message="Successfully delete the webhook with the name of "+str(webhook_name)
              await message.channel.send(full_message)
            if check_bool == False:
              await message.channel.send("You can't use that.")
      except aiohttp.ClientConnectorError:
        await message.channel.send("Not a valid link at all") 
    return

  if message.content.startswith(discordprefix+"webhook_avatar") and not message.author.bot:

    url_used=message.content.split(" ")[1]
    await message.delete()

    async with aiohttp.ClientSession() as cs:
      try:
        async with cs.get(url_used) as response:
          if response.status == 200:
            json_data=await response.json()
            used_id = int(json_data["id"])
            webhook_fetched=await client.fetch_webhook(used_id)
            webhook_avatar=webhook_fetched.avatar_url
            full_info=("The webhook avatar is: \n "+str(webhook_avatar))
            await message.channel.send(full_info)
          if not response.status == 200:
            await message.channel.send("Not a valid link")
      except aiohttp.ClientConnectorError:
        await message.channel.send("Bot ran into an error please try again a bit later.\n Please DM the Bot owner about this")
        
        return
      

    return

  if message.content.startswith(discordprefix+"warn") and not message.author.bot and user.guild_permissions.administrator == True:

    user_info=message.content.replace(discordprefix+"warn ","")

    try:
      user = message.mentions[0]
    except:
      try:
        user = client.get_user(int(user_info.split(" ")[0]))
        if user is None:
          pass
          user = message.author
      except:
        # was the userID not an int?
        pass

    pfp = "https://cdn.discordapp.com/emojis/738229508099801169.png?v=1"

    warn_reason24 = user_info.replace(str(user.id),"")

    warn_reason24 = warn_reason24.replace("<@!>","")

    message_to_send=discord.Embed(title=f"Reason: {warn_reason24} ", color=random.randint(0, 16777215)) 

    message_to_send.set_author(name=f"You have been warned by {message.author}",icon_url=(pfp))

    message_to_send.set_image(url="https://media1.tenor.com/images/e160829e84c01257050490b2dd46c0cb/tenor.gif")
    message_to_send.set_footer(text = f"ID: {message.author.id}")
    
    if (user.dm_channel is None):
      await user.create_dm()
    
    await user.send(embed=message_to_send)

    message_to_send.set_footer(text = f"ID: {message.author.id}\nWarned by {message.author}\nWarned ID: {user.id} \nWarned: {user}")

    channel_used = client.get_channel(738912143679946783)
    await channel_used.send(embed=message_to_send)

    user_warned="Why did you warn "+str(user)+"?"

    

    if (message.author.dm_channel is None):
      await message.author.create_dm()

    await message.author.send(user_warned)

    return


  if message.content.startswith(discordprefix+"open_source") and not message.author.bot:

    pfp = client.user.avatar_url

    source_send=discord.Embed(title="Project at: https://repl.it/@JDJGInc_Offical/JDJGBotSupreme#main.py", description="Want to get more info, contact the owner with the JDBot*owner command",color=random.randint(0, 16777215))

    source_send.set_author(name=f"{client.user} Source Code:",icon_url=(pfp))

    await message.channel.send(embed=source_send)

    return

  if message.content.startswith(discordprefix+"support channel") and not message.author.bot:

    support_msg=message.content.replace(discordprefix+"support channel ","")

    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    
    embed_message = discord.Embed(title=support_msg, description=time_used, color=random.randint(0, 16777215))

    pfp = message.author.avatar_url

    embed_message.set_author(name=f"Help Needed from {message.author}:",icon_url=(pfp))

    embed_message.set_footer(text = f"{message.author.id} \nSupport Mode: Channel")

    embed_message.set_thumbnail(url="https://cdn.discordapp.com/attachments/738912143679946783/763925088378552320/raise_hand.png")



    for cid in send_channel:

      channel_used = client.get_channel(cid)

      embed_message.add_field(name="Sent To:",value=str(channel_used))

      await channel_used.send(embed=embed_message)

    return


  if message.content.startswith(discordprefix+"coin") and not message.author.bot:
    pfp = message.author.avatar_url
    guess_dice=message.content.replace(discordprefix+"coin ","")

    value = random.choice([True,False]) 
    win = False
    if guess_dice.lower().startswith("h") and value:
      win = True
    elif guess_dice.lower().startswith("t") and not value:
      win = True
    elif guess_dice.lower().startswith("h") and not value:
      win = False
    elif guess_dice.lower().startswith("t") and value:
      win = False
    else:
      await message.channel.send("Was that a choice?")
      return
    
    if(value):
      pic_name = "heads"
    else:
      pic_name ="Tails"
    
    if win:
      f = discord.File("./images/"+pic_name+".png",pic_name+".png")
      embed_message = discord.Embed(title="coin flip",color=random.randint(0, 16777215))
      embed_message.set_author(name=f"{message.author}",icon_url=(pfp))
      embed_message.add_field(name="The Coin Flipped: "+("heads" if value else "tails"),value=f"You guessed: {guess_dice}")
      embed_message.add_field(name="Result: ",value="Won")
      embed_message.set_image(url="attachment://"+pic_name+".png")
      await message.channel.send(file = f,embed=embed_message)
    else:
      f = discord.File("./images/"+pic_name+".png",pic_name+".png")
      embed_message = discord.Embed(title="coin flip",color=random.randint(0, 16777215))
      embed_message.set_author(name=f"{message.author}",icon_url=(pfp))
      embed_message.add_field(name="The Coin Flipped: "+("heads" if value else "tails"),value=f"You guessed: {guess_dice}")
      embed_message.add_field(name="Result: ",value="Lost")
      embed_message.set_image(url="attachment://"+pic_name+".png")
      await message.channel.send(file = f,embed=embed_message)
    return

  if message.content.startswith(discordprefix+"webhook_update") and not message.author.bot and message.author.id in jdjg_id:
    update_color = 35056
    await message.delete()
    url_grab = str(os.environ['webhook1'])
    url_grab2 = str(os.environ['webhook99'])
    message_info = message.content.replace(discordprefix+"webhook_update ","")
    url_grab_ultra = [url_grab,url_grab2]
    webhook = discord_webhook.DiscordWebhook(url=url_grab_ultra)
    embed = discord_webhook.DiscordEmbed(title='Update',color=update_color)
    speacil_icon = 'https://media.discordapp.net/attachments/491419169842135059/732821876488798249/fisheye.png'
    embed.add_embed_field(name='Update Info:', value=message_info)
    embed.set_timestamp()
    embed.set_author(name="JDJG's Update",icon_url=speacil_icon)
    embed.set_footer(text="JDJG's Updates")
    webhook.add_embed(embed)
    webhook.execute()
    return

  if message.content.startswith(discordprefix+"insult") and not message.author.bot:
    await message.channel.send("Preparing insult......")
    await asyncio.sleep(1)
    insultt = random.choice(random_response.insult)
    embed = discord.Embed(title = "Here is an insult (at your request)",color=random.randint(0, 16777215))
    embed.add_field(name = "Don't know why you want to insult yourself though?", value = f"{insultt}")
    await message.channel.send(embed=embed)
    return
  
  if message.content.startswith(discordprefix+"send_tweet") and message.author.id in admins and not message.author.bot:

    consumer_key= os.environ['tweet_key']
    consumer_secret=os.environ['tweet_secret']
    access_token=os.environ['tweet_access']
    access_token_secret=os.environ['tweet_token']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth)
    tweet_send=message.content.replace(discordprefix+"send_tweet ","")
    twitter_api.update_status(status = tweet_send)
    return

  if message.content.startswith(discordprefix+"tweet") and not message.author.bot:
    tweet_username = message.content.replace(discordprefix+"tweet ","")
    tweet_number = (tweet_username.split(" ")[-1])
    tweet_username = (tweet_username.split(" ")[0])
    value_before=tweet_number.replace(tweet_username+" ","")
    try:
      value_here = int(value_before)
    except:
      value_here = 20
    
    if value_here > 60:
      value_here = 60
      await message.channel.send("are you insane? Trust me I can DM a lot of tweets... swapping to 60")

    consumer_key= os.environ['tweet_key']
    consumer_secret=os.environ['tweet_secret']
    access_token=os.environ['tweet_access']
    access_token_secret=os.environ['tweet_token']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=tweet_username,count=value_here,tweet_mode="extended")
    tweepy_fetch_user=api.get_user(tweet_username)
    profile_url = str(tweepy_fetch_user.url)
    tweet_info = []
    tweet_urls = []
    for info in tweets:
      tweet_content = info.full_text
      tweet_url = "https://twitter.com/twitter/statuses/"+str(info.id)
      tweet_urls.append(tweet_url)
      tweet_info.append(tweet_content)

    x = 0
    tweet_message_details = ""
    while x < len(tweet_info):
      tweet_url_grab = tweet_urls[x]
      tweet_speacil= tweet_info[x]
      tweet_message_details = tweet_message_details+tweet_speacil+"\n"+str(tweet_url_grab)+"\n"
      x = x + 1

    n = 2000
    split_strings = [tweet_message_details[index : index + n] for index in range(0, len(tweet_message_details), n)]
    x = 0
    pfp = str(tweepy_fetch_user.profile_image_url)
    if (message.author.dm_channel is None):
        await message.author.create_dm()
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_info = discord.Embed(title=f"User Requested: {value_here} messages", description= time_used,color=random.randint(0, 16777215))
    embed_info.set_author(name=f"Tweets from @{tweet_username}",icon_url=(pfp))
    embed_info.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763902909158391858/Twitter.png")
    embed_info.add_field(name="Profile url",value=profile_url)
    embed_info.set_footer(text = f"{message.author.id}")
    await message.author.dm_channel.send(embed=embed_info)

    while x < len(split_strings):

      tweet_message = split_strings[x]

      embed_message = discord.Embed(title="**Tweets:**",description=tweet_message, color=random.randint(0, 16777215))

      await message.author.dm_channel.send(embed=embed_message)

      x = x + 1

    x = 0
    return


  if message.content.startswith(discordprefix+"webhook") and not message.author.bot:
    try:
      webhook_url = message.content.split(" ")[1]
    except:
      await message.channel.send("\n not a valid usage")
      return
    try:
     message_info = message.content.split(" ")[2]
    except:
      message_info = "No content"

    async with aiohttp.ClientSession() as cs:
      async with cs.get(webhook_url) as response:
        if not response.status == 200:
          await message.channel.send("Not a valid link")
          return
        if response.status == 200:
          json_data= await response.json() 
          webhook_name = (json_data["name"])
    

    await message.delete()
    webhook = discord_webhook.DiscordWebhook(url=webhook_url)
    embed = discord_webhook.DiscordEmbed(title=f"Webhook {webhook_name}'s Message:",color=random.randint(0, 16777215))
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed.add_embed_field(name=f"{message_info}", value=time_used)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    return

  if message.content.startswith(discordprefix+"apply bloopers") and not message.author.bot:

    apply_message = message.content.replace(discordprefix+"apply bloopers ","")

    application_user = [
    708167737381486614,
    168422909482762240,
    ]

    await message.delete()

    for x in application_user:

      apply_user = client.get_user(x)

      if (apply_user.dm_channel is None):
        await apply_user.create_dm()

      pfp = message.author.avatar_url

      time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')

      embed_message = discord.Embed(title=apply_message, description=time_used,color=random.randint(0, 16777215))

      embed_message.set_author(name=f"Application from {message.author}",icon_url=(pfp))

      embed_message.set_footer(text = f"{message.author.id}")

      embed_message.set_thumbnail(url="https://cdn.discordapp.com/attachments/738912143679946783/763889399514660914/Ballot.png")


      await apply_user.send(embed=embed_message)

    
    return
      
      
  if message.content.startswith(discordprefix+"radical") and not message.author.bot:

    try:

      num=message.content.split(" ")[1]

      root_int=message.content.split(" ")[2]

    except:

      num = 1

      root_int = 1

    try:

      num_int = int(num)

      root_int = int(root_int)

    except:

      num = int(1)

      root_int = int(1)
      
      await message.channel.send("Why would you use something that isn't a number, try again")



    root_answer = int(root_int**(1/num_int))

    embed = discord.Embed(title = "The Radical Function Has Been Completed!",color=random.randint(0, 16777215))
    embed.set_footer(text = f"{message.author.name} | {message.author.id}")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/d/d1/Calculator_on_macOS.png")
    embed.add_field(name = f"Formula: {num}√ {root_int}", value = f"Result: {root_answer}")

    await message.channel.send(embed=embed)
    channel_usage=client.get_channel(738912143679946783)
    await channel_usage.send(embed=embed)
    return


  if message.content.startswith(discordprefix+"power") and not message.author.bot:

    try:

      num = message.content.split(" ")[1]

      root = message.content.split(" ")[2]

      num_int = int(num)

      root_int = int(root)

      ans = (num_int**root_int)

      embed = discord.Embed(title = f"Result of the function",color=random.randint(0, 16777215))
      embed.add_field(name = f"Formula: {num} ^ {root_int}", value = f"Result: {ans}")
      embed.set_footer(text = f"{message.author.id}")
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/d/d1/Calculator_on_macOS.png")
      await message.channel.send(embed = embed)

    except:

      await message.channel.send("either it was a string you used or you didn't give enough values.")
      
    return

  if message.content.startswith(discordprefix+"works") and not message.author.bot:

    number_here = random.randint(1,100)
    pfp = message.author.avatar_url
    works_time = (message.created_at).strftime('%m/%d/%Y %H:%M:%S')

    try:

      name_1 = message.content.split(" ")[1]

      name_2 = message.content.split(" ")[2] 

      embed_message = discord.Embed(title = f"How well does {name_1} and {name_2} work together?",color=random.randint(0, 16777215))
      embed_message.set_author(name=f"{message.author}",icon_url=(pfp))


      if  number_here  < 50:
        resp = "They don't work well together at ALL :angry:"
      elif number_here < 70 and number_here > 51:
        resp = "They work quite poorly together..."
      elif number_here < 90 and number_here  > 71:
        resp = "They work kinda good together, maybe"
      elif number_here < 99 and number_here > 91:
        resp = "They work REALLY good together, wow. Nice."
      elif number_here == 100:
        resp = "Let them collaborate anytime."
      
      embed_message.add_field(name = f"They work at a rate {number_here}%", value = resp)
      embed_message.set_footer(text = f"{message.author.id} \nTime: {works_time}")
      await message.channel.send(embed=embed_message)

      await client.get_channel(738912143679946783).send(embed=embed_message)

    except:

      await message.channel.send("\n Make sure to have two objects.")

    return

  if message.content.startswith(discordprefix+"this") and not message.author.bot:
    await message.channel.send(message.channel.id)
    return
  if message.content.startswith(discordprefix+"color") and not message.author.bot:

    try:
      convert_from = message.content.split(" ")[1].lower()
      convert_to = message.content.split(" ")[2].lower()
      convert_value = message.content.split(" ")[3].lower()
    except:
      await message.channel.send("Not enough arguments")
      return


    if convert_from == "rgb":
      if convert_value.startswith("("):
        convert_value = convert_value[1:-1]
      triple = convert_value.split(",")
      for i in range(3):
        triple[i] = int(triple[i])
        
    elif convert_from == "hex":
      if convert_value.startswith("#"):
        convert_value = convert_value[1:]
      triple = [convert_value[0:2],convert_value[2:4],convert_value[4:]] #OBOE?
      for i in range(3):
        triple[i] = int(triple[i],16)

    elif convert_from == "decimal":
      triple = discord.Colour(int(convert_value)).to_rgb()

    else:
      await message.channel.send("unknown format: '%s'" % convert_from)
      return

    if convert_to == "rgb":
      converted_value = "(%d,%d,%d)" % tuple(triple)

    elif convert_to == "hex":
      converted_value = "#%02X%02X%02X" % tuple(triple)

    elif convert_to == "decimal":
      c = discord.Colour.from_rgb(*triple)
      converted_value = str(c.value)

    else:
      await message.channel.send("unknown format: '%s'" % convert_to)
      return

    if triple == [255,255,255]:
      triple = [255,254,255]
    color_embed = (discord.Colour.from_rgb(*triple))
    embed = discord.Embed(title = "The conversion has been completed!",description=f"Converted from {convert_from} to {convert_to}:",color=color_embed)
    embed.add_field(name = f"{convert_to}:", value = f"{converted_value}")
    await message.channel.send(embed=embed)

    return
  
  if message.content.startswith(discordprefix+"emote") and not message.author.bot:

    emote_wanted=message.content.replace(discordprefix+"emote ","")
    
    emojiNearest = sorted(client.emojis, key=lambda x: SequenceMatcher(None, x.name, emote_wanted).ratio())[-1]

    await message.channel.send(emojiNearest)

    return

  if message.content.startswith(discordprefix+"servers") and message.author.id in admins and not message.author.bot:
    send_list = [""]
    guild_list = ["%d %s %d %s" % (len(g.members), g.name, g.id, (g.system_channel or g.text_channels[0]).mention) for g in client.guilds]

    for i in guild_list:
      if len(send_list[-1] + i) < 1000:
        send_list[-1] += i + "\n"
      else:
        send_list += [i + "\n"]
    
    if (message.author.dm_channel is None):
      await message.author.create_dm()

    await message.author.dm_channel.send("\n Servers:")

    for i in send_list:
      await message.author.dm_channel.send(i) 
    return

  if message.content.startswith(discordprefix+"message time") and not message.author.bot:

    embed = discord.Embed(title = "Message Time:",color=random.randint(0, 16777215),timestamp=message.created_at)
    embed.set_footer(text=f"{message.author.id}")
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"mail") and not message.author.bot:
    try:
      user = message.mentions[0]
    except:
      try:
        user = client.get_user(int(message.content.split(" ",2)[1]))
          #user does not exist, uses the message.author instead.
      except:
        # was the userID not an int?
        await message.channel.send("\n User Not Found, defaulting to you.")
        pass

    if user is None:
      user = message.author
      await message.channel.send("\n User Not Found, defaulting to you.")
    await message.channel.send("Sending mail....")
    pfp = message.author.avatar_url
    user_id22=str(user.id)
    replace_info="<@!"+str(user.id)+">"
    mail_msg2 = message.content.replace(discordprefix+"mail","")
    mail_msg2 =  mail_msg2.replace(replace_info,"")
    mail_msg2 = mail_msg2.replace(user_id22,"")
    mail_msg2 = mail_msg2.split(" ",2)[-1]
    embed_message = discord.Embed(title=mail_msg2, description=day, color=random.randint(0, 16777215))
    embed_message.set_author(name=f"Mail from: {message.author}",icon_url=(pfp))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url = "https://cdn.discordapp.com/attachments/752527845519130696/763390502317326346/459285aabe618b3d3e215676c97b689c.png")
    if (user.dm_channel is None):
      await user.create_dm()
    await user.send(embed=embed_message)
    embed_message.add_field(name="Sent To:",value=str(user))
    await client.get_channel(738912143679946783).send(embed=embed_message)
    return

  if message.content.lower().startswith('fooz'):
    try:
      evalStr = eval(message.content[4:])
      if evalStr is None or len(str(evalStr)) == 0:
        await message.channel.send("Successful.")
      else:
        await message.channel.send(str(evalStr))
    except Exception as e:
      pass
    return

  for banned_word in banned_words:
    if message.guild == None:
      pass
    elif banned_word in message.content.lower() and not message.guild.id in slur_okay:
      await message.delete()
      banned_response=random.choice(random_response.response_used)
      await message.channel.send(banned_response)
      return

  if message.content.startswith(discordprefix+"clear") or message.content.startswith(discordprefix+"purge"):
    await message.delete()
    user = message.author

    if user.guild_permissions.manage_messages:
      try:
        amount = int(message.content.split(" ")[1])
      except:
        #arguement not an integer
        amount = 0
        pass

      if amount > 100:
        await message.channel.send("Too high set to 100")
        amount = 100                     

      await message.channel.purge(limit = amount)
    return

  if message.content.startswith(discordprefix+"compliment") and not message.author.bot:
    
    complimentt = random.choice(random_response.compliment)

    embed = discord.Embed(title = "Here is a compliment, for you!",color=random.randint(0, 16777215))
    embed.add_field(name = "I hope you like it!", value=complimentt)
    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"Arithmetic") and not message.author.bot:

    try:

      og_number = int(message.content.split(" ")[1])

      per_times = int(message.content.split(" ")[2])

      number_times = int(message.content.split(" ")[3])

      number_result = og_number+per_times*(number_times-1)

      embed = discord.Embed(title = f"Result of the function",color=random.randint(0, 16777215))

      embed.add_field(name=f"Formula: {og_number}+{per_times}*({number_times}-1)",value=f"Result: {number_result}")

      embed.set_footer(text = f"{message.author.id}")
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/d/d1/Calculator_on_macOS.png")

      await message.channel.send(embed=embed)

    except:

      await message.channel.send("Either you forgot the values needed or you used text after the Arithmetic")
    return

  if message.content.startswith(discordprefix+"invite") and not message.author.bot:
    
    embed  = discord.Embed(title = "The Invite Links!", value = "One is for testing, one is the normal bot.",color=random.randint(0, 16777215))
    embed.add_field(name = "Testing Link:", value = "https://discordapp.com/oauth2/authorize?client_id=702243652960780350&scope=bot&permissions=8", inline = False)
    embed.add_field(name = "Normal Invite:", value = "https://discordapp.com/oauth2/authorize?client_id=702238592725942374&scope=bot&permissions=8", inline = False)

    bot_pfp = client.user.avatar_url

    embed.set_thumbnail(url=bot_pfp)

    await message.channel.send(embed=embed)
    return

  if message.content.startswith(discordprefix+"suspend") and message.author.id in admins and not message.author.bot:
    await message.channel.send("suspending bot")
    return
  
  if message.content.startswith(discordprefix+"os") and not message.author.bot:
    if client.os_user == "None":
      client.os_user = message.author.id
      await jdjg_os.os(message)
    return
  
  if message.content.startswith(discordprefix+"spam") and not message.author.bot:
    await message.channel.send("https://tenor.com/view/shoot-spam-gif-11220664")
    return
  
  if message.content.startswith(discordprefix+"classic_delink") and not message.author.bot:
    channel = int(message.content.split(" ")[-1])
    if channel in from_to_channel:
      del from_to_channel[channel]
      await message.channel.send("Linked deleted")
    else:
      await message.channel.send("\n Not a valid Channel.")
    return
  
  if message.content.startswith(discordprefix+"classic_link") and not message.author.bot:
      channel_one = int(message.content.split(" ")[1])
      channel_two = int(message.content.split(" ")[2])
      from_to_channel[channel_one] = channel_two
      try:
        channel_msg = message.content.split(" ", 3)[3]  # everything after the 3rd space is all one string
      except:
        channel_msg = ""
      if channel_msg == "":
        await message.channel.send("Linker set up")
      else:
        await message.channel.send("Message setup message for the link is: "+channel_msg)
      return
    
  if message.content.startswith(discordprefix+"settings") and not message.author.bot:
    import server_settings
    arg = message.content.split(" ")
    #for obj in arg:
    #  print(obj)
    message_return = 0
    print("arg1: "+arg[1]+" arg2: "+arg[2])
    if(arg[1]=="level" and arg[2]=="up" and arg[3]=="message"):
      server_settings.change_setting(message.guild,1,"NULL")
      message_return = 1
    if(arg[1]=="safe" and arg[2]=="server"):
      server_settings.change_setting(message.guild,2,"NULL")
      message_return = 2
    if(arg[1]=="slur" and arg[2]=="ok"):
      args = arg[3:]
      server_settings.change_setting(message.guild,3,args)
      message_return = 3
    if(arg[1]=="prefix" and arg[2]=="change"):
      print(arg[3])
      server_settings.change_setting(message.guild,4,arg[3])
      message_return = 4
    if(arg[1]=="admin" and arg[2]=="add"):
      args = arg[3:]
      server_settings.change_setting(message.guild,5,args)
      message_return = 5
    if(arg[1]=="ban" and arg[2]=="users"):
      args = arg[3:]
      server_settings.change_setting(message.guild,6,args)
      message_return = 6
    if(arg[1]=="test"):
      args = arg[2:]
      mess=""
      for word in args:
        if(len(mess)!=0):
          mess = mess+" "+word
        else:
          mess = mess + word 
      print(mess)
      import swear_checker
      await message.channel.send(swear_checker.censor_message(mess,message.guild.id))
      return
    message_return = message_return -1
    messages = ["Level Up Message","Safe Server","Slur Ok","Prefix","Admin Add","Ban List"]
    if(message_return <5-1):
      await message.channel.send(messages[message_return]+" Toggled!")
    else:
      await message.channel.send(messages[message_return]+ " Added To Database")
    if(message_return==-1):
      await message.channel.send("Invalid Arguments!")
      em = discord.Embed(title="Vaild Commands")
      em.add_field(name="level up", value=".")
      em.add_field(name="safe server", value=".")
      em.add_field(name="slur ok <args>", value=".")
      em.add_field(name="prefix change <new prefix>", value=".")
      em.add_field(name="admin add <admin id>", value=".")
      em.add_field(name="ban users <args>", value=".")
      await message.channel.send(embed=em)
    
    #   1 - Level Up Messages
    #   2 - Safe Server
    #   3 - Slur Ok [args]
    #   4 - prefix change
    #   5 - admin add
    #   6 - Ban List
    #server_settings.change_setting(message.guild,1,"a")
    return

  if message.content.startswith(discordprefix) and not message.author.bot:
    pfp = message.author.avatar_url
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" {message.content}", description=time_used,color=random.randint(0, 16777215))
    embed_message.set_author(name=f"{message.author} tried to excute invalid command:",icon_url=(pfp))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763873708908478474/Warning.png")
    await client.get_channel(738912143679946783).send(embed=embed_message)
    if (message.author.dm_channel is None):
      await message.author.create_dm()
    embed_message = discord.Embed(title=f" {message.content}", description=time_used,color=random.randint(0, 16777215))
    embed_message.set_author(name=f"You tried to excute invalid command:",icon_url=(pfp))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://media.discordapp.net/attachments/738912143679946783/763873708908478474/Warning.png")
    await message.author.dm_channel.send(embed=embed_message)
    return

  for channel_x in from_to_channel:
    if message.channel.id == channel_x:
      channel_id = from_to_channel[channel_x]
      if not message.author.bot:
        await client.get_channel(channel_id).send(message.content)

#RENDEV'S CODE...NO TOUCH
@client.event
async def on_message_delete(message):
  if not message.author.bot:
    #if(message.content=="banana"):
      #import LinkerPort
      #LinkerPort.port()
    em =discord.Embed(title=str(message.author.name)+" Deleted a Message",color=random.randint(0, 16777215))
    if(len(message.content)==0):
      message.content = "NULL"
    em.add_field(name="Message: ",value=message.content)
    await client.get_channel(738912143679946783).send(embed=em)
    try:
     can = await GlobalLinker.FindGlobal(message)
     for obj in can:
        channel = client.get_channel(int(obj["chan_id"]))
        msg= await channel.fetch_message(obj["mes_id"].id)
        await msg.delete()
    except:
      banana = 0
@client.event
async def on_typing(channel,user,_time):
  if not user.bot:
    #try:
    docs = DatabaseConfig.db.g_link_testing.find()
    for chan in docs:
      if (chan["chan_id"]!=channel.id):
       # print("CHAN_ID: "+str(chan["chan_id"]))
        try:
          #print(client.get_channel(int(chan["chan_id"])).name)
          await client.get_channel(int(chan["chan_id"])).trigger_typing()
        except:
          banana = 1
    return
    #except:
  return


@client.event
async def on_message_edit(before,after):
  #print("EDIT")
  if(before.content!=after.content):
    embedVar = discord.Embed(title=before.author.name+" Edited a Message",color=random.randint(0, 16777215))
    embedVar.add_field(name="Before:",value=str(before.content))
    if(len(before.content)==0):
      before.content = "NULL"
    if(len(after.content)==0):
      after.content = "NULL"
    embedVar.add_field(name="After:",value=str(after.content))
    logs = client.get_channel(738912143679946783)
    await logs.send(embed=embedVar)
  if not after.author.bot:
    try:
     can = await GlobalLinker.FindGlobal(before)
     newEmbed = GlobalLinker.GetGlobalEmbed(after)
     for obj in can:
        channel = client.get_channel(int(obj["chan_id"]))
        msg= await channel.fetch_message(obj["mes_id"].id)
        await msg.edit(embed = newEmbed)
    except:
      banana = 0

@client.event
async def on_guild_emojis_update(guild, before, after):
  if emoji_added := [x for x in before if x not in after]:
     for different_emoji in emoji_added:
      logs=client.get_channel(738912143679946783)
      embed = discord.Embed(title=guild.name,color=random.randint(0, 16777215),timestamp=different_emoji.created_at)
      embed.add_field(name=f"{different_emoji.name} deleted",value=f"Animated: {different_emoji.animated}")
      embed.add_field(name="Emojii ID:",value=different_emoji.id)
      embed.set_image(url=different_emoji.url)
      await logs.send(embed=embed)
  if emoji_added := [x for x in after if x not in before]:
    for different_emoji in emoji_added:
      logs=client.get_channel(738912143679946783)
      embed = discord.Embed(title=guild.name,color=random.randint(0, 16777215),timestamp=different_emoji.created_at)
      try:
        emoji=await guild.fetch_emoji(different_emoji.id)
        emoji = emoji.user
      except discord.HTTPException:
          emoji = "Unknown"
      embed.add_field(name=f"{different_emoji.name} added",value=f"Animated: {different_emoji.animated}")
      embed.add_field(name="Emojii ID:",value=different_emoji.id)
      embed.add_field(name="Emote Creator:",value=emoji)
      embed.set_image(url=different_emoji.url)
      await logs.send(embed=embed)
  
  if len(before) == len(after):
    logs=client.get_channel(738912143679946783)
    for x in before:
      for y in after:
        if x.id == y.id:
          if x.name != y.name:
            embed = discord.Embed(title=guild.name,color=random.randint(0, 16777215),timestamp=y.created_at)
            try:
              emoji=await guild.fetch_emoji(x.id)
              emoji = emoji.user
            except discord.HTTPException:
              emoji = "Unknown"
            embed.add_field(name=f"{x.name} edited",value=f"Animated: {y.animated}")
            embed.add_field(name="Emojii ID:",value=y.id)
            embed.add_field(name="Emote Creator",value=emoji)
            embed.add_field(name="New name:",value=y.name)
            embed.set_image(url=y.url)
            await logs.send(embed=embed)
      
          


@client.event
async def on_error(name,*arguments,**karguments):
  import termcolor
  import traceback
  idle_error=traceback.format_exc()
  if len(idle_error) < 2049:
    embed_message = discord.Embed(title="Error:",description=idle_error,color=random.randint(0, 16777215))
    embed_message.add_field(name="More Details:",value=karguments)
    embed_message.set_footer(text=f"Discord details: \n{arguments}")
    idle_error=termcolor.colored(idle_error,"red")
    print(f"\n{idle_error} \n{arguments}")
    try:
      for adID in admin_contact:
        admin_user = client.get_user(adID)
        if (admin_user.dm_channel is None):
          await admin_user.create_dm()
        await admin_user.send(embed=embed_message)
    except:
      print("\n can't DM them")
    await client.get_channel(738912143679946783).send(embed=embed_message)
  if len(idle_error) > 2049:
    idle_error=termcolor.colored(idle_error,"red")
    print(f"\n{idle_error} \n{arguments}")
    print("\n message was way too big for discord")
  a=os.sys.exc_info()
  message_error=arguments[0]
  if isinstance(message_error, discord.Message):
    jdjg = client.get_user(168422909482762240)
    if (jdjg.dm_channel is None):
      await jdjg.create_dm()
    mystbin_client = mystbin.MystbinClient()
    paste = await mystbin_client.post(message_error.content)
    await jdjg.send(f"Error: {paste.url}")
    await mystbin_client.close()
    #try:
      #member_permissions=message_error.channel.permissions_for(message_error.guild.me)
      #if member_permissions.send_messages == True:
        #if(isinstance(a[1],discord.errors.HTTPException)):
          #await message_error.channel.send("Error occuried(please try shorterning your messages)") 
        #if(isinstance(a[1],discord.errors.Forbidden)):
          #await message_error.channel.send("Either you didn't setup the bot right(a.k.a missing permissions) or the bot fell into a cricital error")
    #except discord.errors.Forbidden:
      #pass
    

@client.event
async def on_member_join(member):
  embed_message=discord.Embed(title=f"{member} just joined {member.guild.name}",timestamp=datetime.datetime.utcnow(),color=random.randint(0, 16777215))

  embed_message.set_footer(text=f"User ID: {member.id}")

  await client.get_channel(738912143679946783).send(embed=embed_message)

@client.event
async def on_invite_create(invite):
  try:
    invite.revoked
    invite.guild
    invite.max_age
    invite.code
    print(invite.inviter)
    invite.id
    invite.url
    invite.uses
    creation_date = (invite.created_at).strftime('%m/%d/%Y %H:%M:%S')
  except discord.errors.Forbidden:
    pass

@client.event
async def on_invite_delete(invite):
  try:
    print(invite.revoked)
    print(invite.guild)
    print(invite.max_age)
    print(invite.code)
    print(invite.inviter)
    print(invite.id)
    print(invite.url)
    print(invite.uses)
    creation_date = (invite.created_at).strftime('%m/%d/%Y %H:%M:%S')
    print(creation_date)
  except discord.errors.Forbidden:
    pass


@client.event
async def on_member_remove(member):
  embed_message=discord.Embed(title=f"{member} just left {member.guild.name}",timestamp=datetime.datetime.utcnow(),color=random.randint(0, 16777215))
  embed_message.set_footer(text=f"User ID: {member.id}")
  await client.get_channel(738912143679946783).send(embed=embed_message)

@client.event
async def on_user_update(before,after):
  embed_message = discord.Embed(description=f"{before.mention} **updated their profile!**",color=random.randint(0, 16777215),timestamp=datetime.datetime.utcnow())
  embed_message.set_author(name=f"{before}",icon_url=(after.avatar_url))
  embed_message.set_footer(text=f"User ID: {before.id}")
  if not before.name==after.name:
    embed_message.add_field(name="Username",value=f"{before.name} -> {after.name}")
  if not before.avatar_url == after.avatar_url:
    embed_message.add_field(name="Avatar",value=f"[[before]]({before.avatar_url}) -> [[after]]({after.avatar_url})")
    embed_message.set_thumbnail(url=after.avatar_url)
    embed_message.set_image(url=after.avatar_url)
  if not before.discriminator == after.discriminator:
    embed_message.add_field(name="Discriminator",value=f"#{before.discriminator} -> {after.discriminator}")
  await client.get_channel(738912143679946783).send(embed=embed_message)

@client.event
async def on_guild_remove(guild_fetched):
  channels = [channel for channel in guild_fetched.channels]
  roles = roles= [role for role in guild_fetched.roles]
  embed = discord.Embed(title="Bot just left: "+str(guild_fetched.name), color=random.randint(0,16777215))
  embed.set_thumbnail(url = guild_fetched.icon_url)
  embed.add_field(name='Server Name:',value=f'{guild_fetched.name}')
  embed.add_field(name='Server ID:',value=f'{guild_fetched.id}')
  embed.add_field(name='Server region:',value=f'{guild_fetched.region}')
  embed.add_field(name='Server Creation Date:',value=f'{guild_fetched.created_at}')
  embed.add_field(name='Server Owner:',value=f'{guild_fetched.owner}')
  embed.add_field(name='Server Owner ID:',value=f'{guild_fetched.owner.id}')
  embed.add_field(name='Member Count:',value=f'{guild_fetched.member_count}')
  embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
  embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
  await client.get_channel(738912143679946783).send(embed=embed)


banned_words = [
  'faggot',
  'retard',
  'pussy',
  'bastard',
  'nigga',]

#for banned words a.k.a slurs and such (don't open if you aren't a programmer - or easily offended

credits = """Programmer - Nomic Zorua#6488 
Programmer - JDJG Inc. Official#3493 
Programmer - Shadi#7879(for ranks and such+and some cool new features)- bit of help from him(thank You :D) and korikasyn#0001, as well as RenDev
#2616.
Invite link is https://discordapp.com/oauth2/authorize?client_id=702238592725942374&scope=bot&permissions=8
coded in Python
Open source on https://repl.it/@JDJGInc_Offical/JDJGBotSupreme (check it out) - it's open source so you can see how it works.. Want to help? DM JDJG Inc. Official#3439 and join the support server
We promise it follows(if our bot gets hacked, we will immediately change the token and tell us ourselves, or just join our support server(this makes it easier), some features will be moved to databases, one it makes it possible to store and keeps data private. If you ask what data we have on you, that might take a bit, but our token is stored safetly, as long as none of the project managers leak the info or repl.it isn't hacked(or anything else). the Bot is fine.
Github: https://github.com/JDJGInc/JDJGBotSupreme """

legal_info = """Documents:

https://discord.com/developers/docs/legal

https://discord.com/developers/docs/policy

Api Reference:

https://discord.com/developers/docs/reference

The support server(Discord's):

https://discord.com/invite/discord-developers(discord's developer server(for people like me and Nomic..))

Please contact us if you feel in anyway we might not be following these rules....(this is so we both can be sure we're fine)

We also tell you all the functions it does.. No we don't sell this information, if you do plan to donate, just ask. Though JDJG doesn't really need it..

Alt bot invite:

https://discordapp.com/oauth2/authorize?client_id=702243652960780350&scope=bot&permissions=8

24/7 Hosting by LinuxTerm#8880 (thank you :D)

https://discord.gg/sHUQCch - for another support center"""


token_grab = os.environ['Discordtoken']

B.b()
client.loop.create_task(startup())
client.run(token_grab)

#token_grab uses Discordtoken - for 24/7 bot and Discordtoken2 for testing purposes
#(nightly bot - current open source code)
