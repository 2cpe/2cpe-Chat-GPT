# 
 #
  #
  # Mode By Russia = Instgram 2cpe
 # 
#

#pip install discord.py openai

# import the required libraries
import discord
from discord import Embed
from dotenv import load_dotenv
import os
import openai
import asyncio

# load the environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# initialize the Discord client
client = discord.Client()

# connect to the OpenAI API
openai.api_key = OPENAI_API_KEY

# define the function to generate AI response
async def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024,
            n = 1,
            stop=None,
            timeout=15
        )
        return response.choices[0].text
    except Exception as e:
        print(f"Error in generating response: {e}")
        return None

# define the function to handle incoming messages
@client.event
async def on_message(message):
    # ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # generate 2cpe response for user message
    response = await generate_response(message.content)

    # create an embedded message
    embed = Embed(title="2cpe Response", description=response, color=0x00ff00)

    # send the 2cpe response back to the user as an embedded message
    if response is not None:
        await message.channel.send(embed=embed)

# run the bot
client.run(TOKEN)

