import discord
from discord.ext import commands

tkn = 'YOUR_TOKEN_HERE'
prefix = "."

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	
@client.command()
async def fart(ctx):
	channel = ctx.author.voice.channel
	vc = await channel.connect()
	print("connected to vc")
	vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="audio/fart.ogg"))
    
@client.command() 
async def comedygold(message):
	await message.channel.send("我为中华民国增光添彩")
	
	
@client.command()
async def undertale(message):
	await message.channel.send("Наш образ и Наше подобие, пусть он царствует над рыбами морскими и птицами небесными, над скотом, над всей землей Так Бог сотворил человека по образу Своему, по образу Божьему Он сотворил его; мужчиной и женщиной Он сотворил их. Затем Бог сказал: «Я даю вам все растения с семенами по всей земле и все деревья, дающие плод с семенем внутри; они будут вам в пропитание. 30И всем зверям земным, и всем птицам небесным")
	await message.channel.send(file=discord.File('img/russia.png'))
	
	
	
	
@client.command()
async def polska3d(ctx):
	channel = ctx.author.voice.channel
	vc = await channel.connect()
	print("connected to vc")
	vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="audio/polska.mp4"))
	
client.run(tkn)
