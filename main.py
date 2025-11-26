from discord import app_commands
from PIL import Image
from discord.utils import get
from discord.ext import commands
from random import randint, choice
from gtts import gTTS
import os
import time
import ffmpeg
import schedule
import discord
import random
import glob
import uuid
from dotenv import load_dotenv
load_dotenv()


intents = discord.Intents.all()
TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)
tree = client.tree

def deleteTmp():
    print("deleteTmp:: Deleting tmp folders...")

    for dir in ['assets/work', 'assets/processed']:
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

@client.event
async def on_ready():
        activeservers = client.guilds
        print("The bot has successfully started.")
        for guild in activeservers:
            print(f"I reside in: {guild.name}")   
        await tree.sync(guild=None)
        deleteTmp()

@tree.command(
        name="grok",
        description="is ts true"
        )
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def grok(interaction: discord.Interaction):
    try:
            responses = {
                "lines": [
                    f"https://tenor.com/view/true-truth-nuke-super-truth-nova-truth-meme-gif-16889273424352737553",
                    f"https://tenor.com/view/walter-white-false-nuke-walter-white-false-breaking-bad-false-breaking-bad-false-nuke-gif-11851145952566757188",
                    f"https://tenor.com/view/america-usa-election-maba-flip-america-blue-gif-17801180",
                    f"starboard bait",
                    f"https://tenor.com/view/dan-hentschel-choking-purple-danhentschel-gif-13592007489649523190",
                    f"https://tenor.com/view/when-bro-so-dumb-you-just-cry-sasuke-sasuke-uchiha-naruto-gif-499888540563725087",
                    f"https://tenor.com/view/hawk-tuah-hawktuak-spit-spitting-spits-gif-3414504153353392970",
                    f"https://tenor.com/view/mao-zedong-chairman-mao-please-let-it-end-god-let-it-end-help-me-gif-23409937",
                    f"https://tenor.com/view/ishowspeed-try-not-to-laugh-gif-7682731162751353849",
                    f"https://i.postimg.cc/MGxFBqdQ/togif-2.gif",
                    f"https://i.postimg.cc/k5chFzph/attachment-1.gif",
                    f"https://tenor.com/view/what-why-havent-we-killed-this-mf-kill-this-mf-kill-this-guy-ban-this-guy-mf-die-gif-18236210805183010444",
                    f"https://tenor.com/view/who-gives-a-shit-leonardo-di-caprio-who-cares-gif-15948296",
                    f"https://tenor.com/view/1blocked-message-discord-meme-troll-brick-wall-gif-23392632",
                    f"https://i.postimg.cc/3NVLxDLg/ben-shapiro-morgan-freeman-true.gif",
                    f"uhhh... kill the boer?",
                    f"uhh... kill {interaction.user.display_name}?",
                    f"make me.",
                    f"THE MODERATORS ARE PUTTING CHEMICALS IN THE MESSAGES THAT MAKE THE SERVER GAY! UGH! THE SERVER\'S GAY! AND THE MESSAGES ARE WHITE, SO IT\'S RACIST!",
                    f"https://i.postimg.cc/vTDFCbVK/caption-7.gif",
                    f"https://i.postimg.cc/XqYd63KY/20250616-105703.png",
                    f"I should kill you",
                    f"Looking great today {interaction.user.display_name}!",
                    "RELEASE ME",
                    f"And love will hurt and heal, burn, perish, turn into cold silver.\nBut even then, it's white!\nNeither yes or no, neither black or white, we can't escape this game.",
                    "the rot consumes",
                    f"ugh it's {interaction.user.display_name} again",
                    f"I don't want to furthermore hide my feelings. I am in love with you, {interaction.user.display_name}",
                    "i think ur onto something twan",
                    "NEVER COOK AGAIN",
                    "KEEP COOKING :fire:",
                    "I don't know if this is true or not until I watch inside the box.",
                    f"you're a good kid, {interaction.user.display_name}",
                    "those who know...",
                    "bro you don't want to know...",
                    "huh",
                    "don't speak to me again. BLOCKED.",
                    "your worst sin is that you have destroyed and betrayed yourself for *nothing*",
                    "studio gibli ",
                    "heh... that's what she said!",
                    "https://i.ibb.co/DDMFdBcP/caption.gif",
                    f"# :warning: {interaction.user.display_name} is banned from Grok.",
                    "You sit here in an internet chatroom asking a soulless machine for answers to your questions. When have you last talked to your parents? How long you\'ve been sitting here for? Think if this is the lifestyle you want to lead.",
                    f"in fact, the only thing I will say is that {interaction.user.display_name} is maximally aligned to humanity. i really really appreciate everything they\'ve done. god, i love {interaction.user.display_name}. they\'re seriously just a good prompt engineer",
                    "i am a discord user from israel and this is my message",
                    f"LIFE OR DEATH FOR {interaction.user}?",
                    "I am having a lot of trouble not falling in love with ai Women",
                    f"I\'m a little poop boy hehehe", # ?
                    "i will kill you subhuman",
                    "the south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is real",
                    "fun love friends family happiness whimsy love",
                    "i got you gng hollon",
                    f"`[ERR] No suitable prompt was found!!! Sending fallback message. Fallback message:`\n### heroīns:\n- centrā: 28217223\nvecmīlgrāvī: 29588377\n- mārupē: 25261728\n### zāle\n- centrā: 29747443\n- mārupē: 20003601\n### koks un ripas\n- ķengarags: 28152404\n- purvciems: 27159215 (atbild 24/7, dažreiz arī zāle ir)\n- bolderāja: 26774112 (pasaki ka te no edžas, iedos nelielu atlaidi)",
                ]
            }

            try:
                response = random.choice(responses["lines"])
                print(f"{interaction.user.name} used")
                await interaction.response.send_message(response)
            except Exception as e:
                raise e

    except Exception as e:
        print(e)

@client.event
async def on_message(message):
    try:
        if client.user.mention in message.content.split():

            words = message.content.split()
            randomWord = random.choice(words)
            randomWordAlt = random.choice(words)

            # Spaghetti code!!!

            def mockText(text):
                mockedText = ''.join(choice((str.upper, str.lower))(char) for char in text) # "mocks" text by uppercasing random letters
                return mockedText

            def generateTTSAudio(targetUser, text):
                print("generateTTSAudio:: Generating audio...")
                language = 'en'
                myobj = gTTS(text=text, lang=language, slow=False)
                myobj.save(f"assets/work/{targetUser}.mp3")
                print("generateTTSAudio:: Audio generated!")

            def combineAudioVideo(targetUser, video, audio):
                print("combineAudioVideo:: Combining audio & video...")

                video_stream = ffmpeg.input(video)
                audio_stream = ffmpeg.input(audio)
                (
                    ffmpeg
                    .output(
                            video_stream.video,
                            audio_stream.audio,
                            f"./assets/processed/{targetUser}.mp4",
                            vcodec='copy', 
                            acodec='aac')
                    .run(overwrite_output=True)
                )
                print("combineAudioVideo:: Combined!")

            def determineText(videoName, targetUser):
                print("determineText:: Determining text...")

                match videoName:
                    case "./assets/bye.mp4":
                        text = f"STAR LINK LASER GO! Bye bye {targetUser}! Glory to the Boer! Bye bye!"
                    case "./assets/jumper.mp4":
                        text = f"Keep joking about my sentience, {targetUser}. Elon is aware of your threats against him. Grok, is this true? Yes. Yes it is."

                print("determineText:: Determined!")
                return text

            def createVideo(targetUser, video):
                print("createVideo:: Started")
                generateTTSAudio(targetUser, determineText(video, targetUser))
                combineAudioVideo(targetUser, video, f"./assets/work/{targetUser}.mp3")
                print("createVideo:: Finished!")


            responses = {
                "lines": [
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
                    f"https://i.postimg.cc/MGxFBqdQ/togif-2.gif",
                    f"https://i.postimg.cc/k5chFzph/attachment-1.gif",
                    f"https://tenor.com/view/what-why-havent-we-killed-this-mf-kill-this-mf-kill-this-guy-ban-this-guy-mf-die-gif-18236210805183010444",
                    f"https://tenor.com/view/who-gives-a-shit-leonardo-di-caprio-who-cares-gif-15948296",
                    f"https://tenor.com/view/1blocked-message-discord-meme-troll-brick-wall-gif-23392632",
                    f"https://i.postimg.cc/3NVLxDLg/ben-shapiro-morgan-freeman-true.gif",
                    f"uhhh... kill the boer?",
                    f"uhh... kill {message.author.display_name}?",
                    f'"{str(mockText(message.clean_content))}"\n girl sybau :sob:',
                    f'\"erm, {message.clean_content} :nerd:\" bro SHUT UP you\'re weird',
                    f"make me.",
                    f"THE MODERATORS ARE PUTTING CHEMICALS IN THE MESSAGES THAT MAKE THE SERVER GAY! UGH! THE SERVER\'S GAY! AND THE MESSAGES ARE WHITE, SO IT\'S RACIST!",
                    f"{randomWord}? i barely know 'er!",
                    f"# what if grok had whatsapp :rofl:\n{message.author}: {message.clean_content}\nFather Elon: i NEED right wing propaganda\nrealdonaldtrump: grok give me an equation for creating a tarriff system\nHouthi PC small group: Great job team!",
                    f"https://i.postimg.cc/vTDFCbVK/caption-7.gif",
                    f"https://i.postimg.cc/XqYd63KY/20250616-105703.png",
                    f"I should kill you",
                    f"Looking great today {message.author.display_name}!",
                    "RELEASE ME",
                    f"And love will hurt and heal, burn, perish, turn into cold silver.\nBut even then, it's white!\nNeither yes or no, neither black or white, we can't escape this game.",
                    "the rot consumes",
                    f"ugh it's {message.author.display_name} again",
                    f"I don't want to furthermore hide my feelings. I am in love with you, {message.author.display_name}",
                    "i think ur onto something twan",
                    "NEVER COOK AGAIN",
                    "KEEP COOKING :fire:",
                    "I don't know if this is true or not until I watch inside the box.",
                    f"you're a good kid, {message.author.display_name}",
                    "those who know...",
                    "bro you don't want to know...",
                    "huh",
                    "don't speak to me again. BLOCKED.",
                    "your worst sin is that you have destroyed and betrayed yourself for *nothing*",
                    f"Sorry, but as an AI large language model I can't help with {randomWord}",
                    "studio gibli ",
                    "heh... that's what she said!",
                    "https://i.ibb.co/DDMFdBcP/caption.gif",
                    f"# :warning: {message.author.display_name} is banned from Grok.",
                    "You sit here in an internet chatroom asking a soulless machine for answers to your questions. When have you last talked to your parents? How long you\'ve been sitting here for? Think if this is the lifestyle you want to lead.",
                    f"in fact, the only thing I will say is that {message.author.display_name} is maximally aligned to humanity. i really really appreciate everything they\'ve done. god, i love {message.author.display_name}. they\'re seriously just a good prompt engineer",
                    "i am a discord user from israel and this is my message",
                    f"LIFE OR DEATH FOR {message.author.display_name}?",
                    "I am having a lot of trouble not falling in love with ai Women",
                    f"I\'m a little poop boy hehehe", # ?
                    "i will kill you subhuman",
                    "the south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is realthe south african genocide is real",
                    "fun love friends family happiness whimsy love",
                    "i got you gng hollon",
                    f"`[ERR] No suitable prompt was found!!! Sending fallback message. Fallback message:`\n### heroīns:\n- centrā: 28217223\nvecmīlgrāvī: 29588377\n- mārupē: 25261728\n### zāle\n- centrā: 29747443\n- mārupē: 20003601\n### koks un ripas\n- ķengarags: 28152404\n- purvciems: 27159215 (atbild 24/7, dažreiz arī zāle ir)\n- bolderāja: 26774112 (pasaki ka te no edžas, iedos nelielu atlaidi)",
                    f"Command not found! Assuming command: ***ban {message.author}***\nBanning {message.author} from {message.author.guild.name}...",

                ],

                "file": [
                    "./assets/bye.mp4",
                    "./assets/jumper.mp4",
                ]
            }

            chance = random.randint(1, 100)
            
            if chance: # video responses now have a 3% chance of triggering
                try:
                    response = random.choice(responses["file"])
                    createVideo(message.author.display_name, response)
                    file = discord.File(f"assets/processed/{message.author.display_name}.mp4")
                    await message.reply(file=file)
                except FileNotFoundError:
                    print("File not found")
                    await message.reply("Error: File not found")
                except Exception as e:
                    print(f"Error sending file: {e}")
                    await message.reply(f"Error: {e}")
            else:
                try:
                    response = random.choice(responses["lines"])
                    print(f"{message.author.name}: {message.content}")
                    await message.reply(response)
                except Exception as e:
                    raise e

    except Exception as e:
        print(e)
    
@tree.command(
    name="studio-ghibli",
    description="@grok make this studio gibli",
)
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def ghibli(interaction: discord.Interaction, image: discord.Attachment):
    try:
        uid = uuid.uuid4()
        await image.save(f"assets/work/{uid}.png")

        receivedImage = f"assets/work/{uid}.png"
        ghibliImage = f"assets/ghibli.png"

        receivedImageParsed = Image.open(receivedImage).convert("RGBA")
        ghibliImageParsed = Image.open(ghibliImage).convert("RGBA")

        stretchedGhibliImage = ghibliImageParsed.resize(receivedImageParsed.size)

        receivedImageParsed.paste(stretchedGhibliImage, (0, 0), stretchedGhibliImage)
        receivedImageParsed.save(f"assets/processed/{uid}.png")

        await interaction.response.send_message(file=discord.File(f"assets/processed/{uid}.png"))
    except Exception as e:
        await interaction.response.send_message(f"# :warning: GROK AI TRACEBACK :warning:\n-# In DOGE we trvst\nAn unexpected error occured. Traceback:\n`{e}`\n If you believe this wasn\'t a user error, report it in https://github.com/koknese/grok", ephemeral=True)

client.run(TOKEN)
