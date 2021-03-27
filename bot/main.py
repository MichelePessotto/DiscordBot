import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  print('Someone wrote a message')

  if message.author == client.user:
    return
  
  if message.content.startswith('!Hello'):
    await message.channel.send('Hello!')

@client.event
async def on_voice_state_update(member, before, after):
  print('New user has entered voice channel')

  if not before.channel:
    channel = client.get_channel(652936968774221864)
    await channel.send(f'{member.name} è entrato nel canale vocale {after.channel.name}')

client.run(os.getenv('TOKEN'))