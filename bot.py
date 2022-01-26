import random
from datetime import datetime
import discord

command = "+"
def get_msg_random(message):
	try:
		message.split()[1]
		message.split()[2]
	except IndexError:
		return "'랜덤 min max' 형식으로 입력해 주세요."
	try:
		rd = random.randint(int(message.split()[1]), int(message.split()[2]))
	except ValueError:
		return "제대로된 숫자를 입력하지 않았습니다."
	return rd
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
	if message.content.startswith(command+"랜덤"):
		rd = str(get_msg_random(message.content))
		await message.channel.send(rd)
clt.run("token")