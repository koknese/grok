from discord import app_commands
from discord.utils import get
from discord.ext import commands
from random import randint
import os
import discord
import random
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()
TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

@client.event
async def on_ready():
    print("The bot has successfully started.")

@client.event
async def on_message(message):
    try:
        if client.user.mention in message.content.split():
            words = message.content.split()
            randomWord = random.choice(words)
            randomWordAlt = random.choice(words)

            lines = [
                f"Did you know that {randomWord} massively funds zionist lobbies?",
                f"Yes, {randomWord} is redacted in JFK files.",
                f"***Readers added context they thought people might want to know***\n{randomWord} is {randomWordAlt}.",
                f"https://tenor.com/view/true-truth-nuke-super-truth-nova-truth-meme-gif-16889273424352737553",
                f"https://tenor.com/view/walter-white-false-nuke-walter-white-false-breaking-bad-false-breaking-bad-false-nuke-gif-11851145952566757188",
                f"https://tenor.com/view/america-usa-election-maba-flip-america-blue-gif-17801180",
                f"starboard bait",
                f"{randomWord} is fake and gay",
                f"@Grok is this {randomWord}?"
            ]

            response = random.choice(lines)
            await message.reply(response)
    except Exception as e:
        print(e)
    
client.run(TOKEN)

