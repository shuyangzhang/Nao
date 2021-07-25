from khl import TextMsg, Bot, Cert
from dotenv import load_dotenv
import os
import traceback

from daily_mission.daily import daily_mission


load_dotenv()

client_id = os.environ.get("CLIENT_ID")
token = os.environ.get("TOKEN")
client_secret = os.environ.get("CLIENT_SECRET")

DEBUG = False

cert = Cert(
            client_id=client_id,
            client_secret=client_secret,
            token=token
        )
bot = Bot(cmd_prefix=["!", "！"], cert=cert)

#@bot.command(name="hello")
#async def roll(msg: TextMsg):
#    await msg.ctx.send("different")
#    await msg.reply("world!")
#    print(msg.channel_id, msg.channel_name, msg.guild_id, msg.author)
#    await msg.reply_temp(f"author_id: {msg.author_id} temp message", temp_target_id = msg.author_id)

@bot.command(name="ping")
async def ping(msg: TextMsg):
    await msg.ctx.send("pong!")

@bot.command(name="debug")
async def debug(msg: TextMsg):
    if msg.author.id in ["693543263"]:
        global DEBUG
        DEBUG = not DEBUG
        if DEBUG:
            await msg.ctx.send("debug switch is on")
        else:
            await msg.ctx.send("debug switch is off")
    else:
        await msg.ctx.send("permission denied")

# cdkey_sent_list = {}

# @bot.command(name="cdkey")
# async def cdkey(msg: TextMsg):
#     # author_me = await msg.ctx.bot.get("https://www.kaiheila.cn/api/v3/user/me")
#     global cdkey_sent_list
#     if msg.author.id not in cdkey_sent_list:
#         cdkey_sent_list[msg.author.id] = msg.author.id
#         await msg.ctx.send(f"hi, {msg.author.id}, cdkey is sent to you, pls check your PM.")
#         content = "your cdkey is AAAA-BBBB-CCCC"
#         await msg.reply_temp(content)
# #        await msg.ctx.bot.post("https://www.kaiheila.cn/api/v3/direct-message/create",json={"target_id":msg.author.id, "content":content})
#         await msg.ctx.bot.post("https://www.kaiheila.cn/api/v3/message/add-reaction", json={"msg_id": msg.msg_id, "emoji": "ballot_box_with_check"})
#     else:
#         await msg.ctx.send(f"hi, {msg.author.id}, you have already received.")
#         await msg.ctx.bot.post("https://www.kaiheila.cn/api/v3/message/add-reaction", json={"msg_id": msg.msg_id, "emoji": "cross_mark_button"})

# @bot.command(name="sentlist")
# async def sentlist(msg: TextMsg):
#     global cdkey_sent_list
#     await msg.ctx.send(f"these users have recieved cdkeys: {cdkey_sent_list}")

@bot.command(name="daily", aliases=["每日", "日常"])
async def daily(msg: TextMsg):
    try:
        daily_mission_text = await daily_mission()
        await msg.ctx.send(daily_mission_text)
    except:
        if DEBUG:
            await msg.ctx.send(traceback.format_exc())

@bot.command(name="logout")
async def logout(msg: TextMsg):
    if msg.author.id in ["693543263"]:
        await msg.ctx.send("logging out now...")
        raise KeyboardInterrupt()
    else:
        await msg.ctx.send("permission denied")

bot.run()