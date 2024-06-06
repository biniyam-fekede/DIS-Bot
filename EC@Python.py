import discord
import os
import random 
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

load_dotenv()

#
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

#
token = str(os.getenv('TOKEN'))


print('This is my Ec2_metadata.region:', ec2_metadata.region)
print('This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)

@client.event 
async def on_ready(): 
#
 print("Logged in as a bot {0.user}".format(client))

@client.event 
async def on_message(message): 
    # 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 

    # 
    print(f'Message {user_message} by {username} on {channel}') 

    # 
    if message.author == client.user: 
        return
    # Check if the message is in the "random" channel
    if channel == "random": 
        # Respond to greetings
        if user_message.lower() == "hey":
            await message.channel.send(f'Hi {username}') 
            return
        # other string options
        elif user_message.lower() == "whatsauuuuup": 
            await message.channel.send(f'amesegnalew {username}') 

        # Returning instance data for the last conditional statement.
        elif user_message.lower() == "ec2 data": 
            await message.channel.send(f"Your instance data is  {ec2_metadata.instance_id} Your EC2 Data: {ec2_metadata.region}") 

#Run the bot with the token
client.run(token)
