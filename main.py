import discord
from discord.ext import commands
from settings import api
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            fileName = attachment.filename
            url = attachment.url
            await attachment.save(f"{os.path.join("images",fileName)}")
            await ctx.send("image saved\t" + url)
    else:
        await ctx.send("resim yüklemeyi unuttun")
    

bot.run(api["key"])