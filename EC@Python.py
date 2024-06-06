import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

# Load environment variables from .env file
load_dotenv()

# Configure Discord intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

# Retrieve the bot token from environment variables
token = os.getenv('TOKEN')

# Print EC2 metadata for debugging purposes
try:
    print('This is my EC2 metadata region:', ec2_metadata.region)
    print('This is my EC2 metadata instance ID:', ec2_metadata.instance_id)
except Exception as e:
    print(f"Error retrieving EC2 metadata: {e}")

@client.event
async def on_ready():
    print(f"Logged in as bot {client.user}")

@client.event
async def on_message(message):
    # Get the username, channel name, and message content
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    # Log the message
    print(f'Message from {username} in {channel}: {user_message}')

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message is in the "random" channel
    if channel == "random":
        # Respond to greetings
        if user_message.lower() == "hey":
            await message.channel.send(f'Hi {username}')
        elif user_message.lower() == "whatsauuuuup":
            await message.channel.send(f'amesegnalew {username}')
        elif user_message.lower() == "ec2 data":
            try:
                instance_id = ec2_metadata.instance_id
                region = ec2_metadata.region
                await message.channel.send(f"Your instance data: Instance ID - {instance_id}, Region - {region}")
            except Exception as e:
                await message.channel.send(f"Error retrieving EC2 data: {e}")

# Run the bot with the token
client.run(token)
