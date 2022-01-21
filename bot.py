from datetime import datetime
import discord

command = "+"
clt = discord.Client()
@clt.event
async def on_ready():
	print("{0.user}으로 로그인됨".format(clt))
@clt.event
async def on_message(message):
	if message.author == clt.user:
		return
	if message.content.startswith(command+"안녕"):
		await message.channel.send(str(message.author)+"님 안녕하세요?")
	if message.content.startswith(command+"오늘"):
		await message.channel.send("오늘은 "+str(datetime.now().year)+"년 "+str(datetime.now().month)+"월 "+str(datetime.now().day)+"일 입니다.")

clt.run("token")