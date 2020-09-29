import os
import logging
import asyncio
import discord
os.system("title Ready to delete!")
from discord.ext import commands
TOKEN = "ABC123"
bot = commands.Bot(description="Discord self-bot" , command_prefix="!")






@bot.event
async def on_connect():
	print(f"Connected to {bot.user.name} :)" )
	
	
@bot.event
async def on_ready():
	print(f"Ready to mess with {bot.user.name} :)" )
    



@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        await message.delete()
        print(f"[!] Deleted {message.content}")
        os.system(f"title [!] Deleted {message.content}")
    else:
        pass
    

bot.run(TOKEN, bot = False)


