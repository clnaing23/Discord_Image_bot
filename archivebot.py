import discord
import os
from dotenv import load_dotenv

#loads discord token
load_dotenv()
TOKEN = os.getenv('TOKEN')


client = discord.Client()
#type of images that the server accepts
image_types=('.jpg','.png','.gif','.jpeg', '.jfif')

#tells user that the bot is ready and online
@client.event
async def on_ready():
    general_channel = client.get_channel(870090704603451396)
    await general_channel.send('I am ready to organize pictures!')
#allows the user to tell the bot to upload files from directory
@client.event
async def on_message(message):
    #channels
    animal_channel = client.get_channel(870480927661383721)
    car_channel = client.get_channel(870305067293618186)
    anime_channel = client.get_channel(870485210188349511)
    meme_channel = client.get_channel(870486123057668136)
    reaction_channel = client.get_channel(870490301050015745)
    general_channel = client.get_channel(870090704603451396)
    #for general channel. General channels works as a utility channel
    if message.content == "upload" or message.content == "Upload":
        #list of the contents of directory
        root_dir = os.listdir('./Pictures')
        for filename in root_dir:
            if filename.endswith(image_types):
                #in case file is too big or other error
                try:
                    #allows for program to find the path for the file in directory
                    with open(os.path.join('./Pictures', filename), 'rb') as fp:
                        #pushes image onto server
                        await general_channel.send(file=discord.File(fp, filename))
                    #Removes image from directory so the image won't be uploaded again and save user storage space
                    os.remove(os.path.join('./Pictures', filename))
                except:
                    await general_channel.send('Sorry, that can not be upload')
    #Each if statement allows for user to upload all content from folder into a specific folder if all pictures are same type
    #Each if statement contains multiple conditions in order to make allow the user more than one way to trigger it 
    if message.content == "car" or message.content == "car" or message.content =="cars" or message.content=="Cars":
        root_dir = os.listdir('./Pictures')
        for filename in root_dir:
            if filename.endswith(image_types):
                try:
                    with open(os.path.join('./Pictures', filename), 'rb') as fp:
                        await car_channel.send(file=discord.File(fp, filename))
                    os.remove(os.path.join('./Pictures', filename))
                except:
                    await general_channel.send('Sorry, that can not be upload')
    if message.content == "animal" or message.content == "Animal" or message.content == "animals" or message.content == "content":
        root_dir = os.listdir('./Pictures')
        for filename in root_dir:
            if filename.endswith(image_types):
                try:
                    with open(os.path.join('./Pictures', filename), 'rb') as fp:
                        await animal_channel.send(file=discord.File(fp, filename))
                    os.remove(os.path.join('./Pictures', filename))
                except:
                    await general_channel.send('Sorry, that can not be upload')
    if message.content == "meme" or message.content == "Meme" or message.content == "memes" or message.content == "Memes":
        root_dir = os.listdir('./Pictures')
        for filename in root_dir:
            if filename.endswith(image_types):
                try:
                    with open(os.path.join('./Pictures', filename), 'rb') as fp:
                        await meme_channel.send(file=discord.File(fp, filename))
                    os.remove(os.path.join('./Pictures', filename))
                except:
                    await general_channel.send('Sorry, that can not be upload')
    if message.content == "anime" or message.content == "Anime":
        root_dir = os.listdir('./Pictures')
        for filename in root_dir:
            if filename.endswith(image_types):
                try:
                    with open(os.path.join('./Pictures', filename), 'rb') as fp:
                        await anime_channel.send(file=discord.File(fp, filename))
                    os.remove(os.path.join('./Pictures', filename))
                except:
                    await general_channel.send('Sorry, that can not be upload')
    if message.content == "reaction" or message.content == "Reactions" or message.content == "reactions" or message.content == "Reaction":
        root_dir = os.listdir('./Pictures')
        for filename in root_dir:
            if filename.endswith(image_types):
                try:
                    with open(os.path.join('./Pictures', filename), 'rb') as fp:
                        await reaction_channel.send(file=discord.File(fp, filename))
                    os.remove(os.path.join('./Pictures', filename))
                except:
                    await general_channel.send('Sorry, that can not be upload')
#allows for user to assign images to a specific channel with a specific reaction from general channel
@client.event
async def on_raw_reaction_add(payload):
    #channels
    general_channel = client.get_channel(870090704603451396)
    animal_channel = client.get_channel(870480927661383721)
    car_channel = client.get_channel(870305067293618186)
    anime_channel = client.get_channel(870485210188349511)
    meme_channel = client.get_channel(870486123057668136)
    reaction_channel = client.get_channel(870490301050015745)
    #checks to ensure that the reaction happened in general channel
    if (payload.channel_id == 870090704603451396):
        #finds message information from message id
        message = await general_channel.fetch_message(payload.message_id)
        # for animal channel
        #each server is represented by a unicode emoji
        if (payload.emoji.name == "🐶"):
            try:
                #copied link of message then sends it to corresponding channel
                await animal_channel.send(message.attachments[0].url)
            except:
                general_channel.send("Sorry, something went wrong")
        #car channel
        elif (payload.emoji.name == "🚙"):
            try:
                await car_channel.send(message.attachments[0].url)
            except:
                general_channel.send("Sorry, something went wrong")
        #anime channel
        elif (payload.emoji.name == "🗾"):
            try:
                await anime_channel.send(message.attachments[0].url)
            except:
                general_channel.send("Sorry, something went wrong")
        #meme channel
        elif (payload.emoji.name == "😆"):
            try:
                await meme_channel.send(message.attachments[0].url)
            except:
                general_channel.send("Sorry, something went wrong")
        #reaction channel
        elif (payload.emoji.name == "🇷"):
            try:
                await reaction_channel.send(message.attachments[0].url)
            except:
                general_channel.send("Sorry, something went wrong")

#runs bot
client.run(TOKEN)