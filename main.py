from discord import app_commands
from discord.utils import get
from discord.ext import commands
from random import randint, choice
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
        activeservers = client.guilds
        print("The bot has successfully started.")
        for guild in activeservers:
            print(f"I reside in: {guild.name}")   

@client.event
async def on_message(message):
    try:
        if client.user.mention in message.content.split():
            words = message.content.split()
            randomWord = random.choice(words)
            randomWordAlt = random.choice(words)
            
            def mockText(text):
                mockedText = ''.join(choice((str.upper, str.lower))(char) for char in text) # "mocks" text by uppercasing random letters
                return mockedText

            lines = [
                f"Did you know that {randomWord} massively funds zionist lobbies?",
                f"Yes, {randomWord} is redacted in JFK files.",
                f"***Readers added context they thought people might want to know***\n{randomWord} is {randomWordAlt}.",
                f"https://tenor.com/view/true-truth-nuke-super-truth-nova-truth-meme-gif-16889273424352737553",
                f"https://tenor.com/view/walter-white-false-nuke-walter-white-false-breaking-bad-false-breaking-bad-false-nuke-gif-11851145952566757188",
                f"https://tenor.com/view/america-usa-election-maba-flip-america-blue-gif-17801180",
                f"starboard bait",
                f"{randomWord} is fake and gay",
                f"@Grok is this {randomWord}?",
                f"https://tenor.com/view/dan-hentschel-choking-purple-danhentschel-gif-13592007489649523190",
                f"https://tenor.com/view/when-bro-so-dumb-you-just-cry-sasuke-sasuke-uchiha-naruto-gif-499888540563725087",
                f"https://tenor.com/view/hawk-tuah-hawktuak-spit-spitting-spits-gif-3414504153353392970",
                f"https://tenor.com/view/mao-zedong-chairman-mao-please-let-it-end-god-let-it-end-help-me-gif-23409937",
                f"https://tenor.com/view/ishowspeed-try-not-to-laugh-gif-7682731162751353849",
                f"https://cdn.discordapp.com/attachments/1321542534509367388/1322551688812298292/togif.gif?ex=684d743e&is=684c22be&hm=317258b2c0d7747df58ae455d453a5c8c7caa890b2bee28dd9eb6e0be34d7541&",
                f"https://cdn.discordapp.com/attachments/1220704562948608001/1287516851286315121/attachment.gif?ex=684d3842&is=684be6c2&hm=08dedafbd341ecfd1d7fb8647b9565d2346e0e9f4e855b737232ddc6167b87c3&",
                f"https://tenor.com/view/what-why-havent-we-killed-this-mf-kill-this-mf-kill-this-guy-ban-this-guy-mf-die-gif-18236210805183010444",
                f"https://tenor.com/view/who-gives-a-shit-leonardo-di-caprio-who-cares-gif-15948296",
                f"https://tenor.com/view/1blocked-message-discord-meme-troll-brick-wall-gif-23392632",
                f"https://cdn.discordapp.com/attachments/977196983573938208/1265730710631878777/ben-shapiro-morgan-freeman-true.gif?ex=684d1055&is=684bbed5&hm=1f4da98290d201666aa74b6c52aa696893ec2c7e8bd6978d1886e347536d8b92&",
                f"uhhh... kill the boer?",
                f"uhh... kill {message.author}?",
                f'"{str(mockText(message.clean_content))}"\n girl sybau :sob:',
                f'\"erm, {message.clean_content} :nerd:\" bro SHUT UP you\'re weird',
                f"make me.",
                f"THE MODERATORS ARE PUTTING CHEMICALS IN THE MESSAGES THAT MAKE THE SERVER GAY! UGH! THE SERVER\'S GAY! AND THE MESSAGES ARE WHITE, SO IT\'S RACIST!",
                f"{randomWord}? i barely know 'er!",
                f"# what if grok had whatsapp :rofl:\n{message.author}: {message.clean_content}\nFather Elon: i NEED right wing propaganda\nrealdonaldtrump: grok give me an equation for creating a tarriff system\nHouthi PC small group: Great job team!",
            ]

            response = random.choice(lines)
            await message.reply(response)
    except Exception as e:
        print(e)
    
client.run(TOKEN)

