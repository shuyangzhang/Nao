from khl import Message, Bot, Event, EventTypes
from dotenv import load_dotenv
import os
import traceback

from daily_mission.daily import daily_mission


load_dotenv()

token = os.environ.get("TOKEN")

DEBUG = False

bot = Bot(token=token)

@bot.command(name="ping")
async def ping(msg: Message):
    await msg.channel.send("pong!")

@bot.command(name="debug")
async def debug(msg: Message):
    if msg.author.id in ["693543263"]:
        global DEBUG
        DEBUG = not DEBUG
        if DEBUG:
            await msg.channel.send("debug switch is on")
        else:
            await msg.channel.send("debug switch is off")
    else:
        await msg.channel.send("permission denied")

    await msg.channel.send(f"these users have recieved cdkeys: {cdkey_sent_list}")

@bot.command(name="daily", aliases=["每日", "日常"])
async def daily(msg: Message):
    try:
        daily_mission_text = await daily_mission()
        await msg.channel.send(daily_mission_text)
    except:
        if DEBUG:
            await msg.channel.send(traceback.format_exc())

@bot.command(name="logout")
async def logout(msg: Message):
    if msg.author.id in ["693543263"]:
        await msg.channel.send("logging out now...")
        raise KeyboardInterrupt()
    else:
        await msg.channel.send("permission denied")

bot.run()