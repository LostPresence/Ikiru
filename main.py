import discord
from discord import client
from discord.ext import commands
import os
from discord.ext.commands.core import bot_has_any_role
import random 
import dotenv


intents = discord.Intents.all()


bot = commands.Bot( command_prefix = "$", intents=intents)

dotenv.load_dotenv() 

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
	await ctx.send("Hello I am Ikiru Bot!")

@bot.event 
async def on_message(message):
	if message.author == bot.user :
		return

	if message.content.startswith('What'):
		return await message.channel.send ('Yajurva is Sleeping!')

	await bot.process_commands(message)

@bot.command()
async def goodbye(ctx):
	await ctx.send("I Hope You Stayed For Longer, But Goodbye")

@bot.command()
async def whyareugood(ctx):
	await ctx.send("Because my bf Ikiru Made me")

@bot.event
async def on_member_join(member):
	print(f'{member} has joined Homies.')

@bot.command()
async def ping(ctx):
	await ctx.send(f'Your Ping is {round(bot.latency * 100)}ms')

client = discord.client
keywords = ["Yesn't"]

@bot.event
async def on_message(message):
    for word in keywords:
        if not word in message.content:
          continue

        for j in range(40):
          await message.channel.send("Dont Use This Command Right Now Dumbo")



bot.run(os.environ["TOKEN"])