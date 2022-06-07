import datetime

from khl import Bot
from app.utils.channel_utils import update_channel_name_by_bot


ERINN_TIME_PER_MIN = 1500   # ms
ERINN_TIME_PER_HOUR = 60 * ERINN_TIME_PER_MIN
ERINN_TIME_PER_DAY = 24 * ERINN_TIME_PER_HOUR

ERINN_TIME_CHANNEL_ID = "6600928158010205"
SERVER_TIME_CHANNEL_ID = "7053938039769278"
LOCAL_TIME_CHANNEL_ID_LIST = [
        "6358058041876630",
        "4012778954789260",
        "6989414216725597",
        "4621353287497441",
    ]
TOKYO_TIME_CHANNEL_ID_LIST = [
        "4699034298526960",
    ]

async def get_local_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    time_str = datetime.datetime.strftime(now, "%H:%M %p")
    return time_str

async def get_tokyo_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    time_str = datetime.datetime.strftime(now, "%H:%M %p")
    return time_str

async def get_server_time():
    server_now = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
    time_str = datetime.datetime.strftime(server_now, "%H:%M %p")
    return time_str

async def get_erinn_time():
    server_now = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
    server_today_truncated = server_now.replace(hour=0, minute=0, second=0, microsecond=0)
    duration = server_now - server_today_truncated
    duration_ms = int(duration.total_seconds() * 1000)
    erinn_today_ms = duration_ms % ERINN_TIME_PER_DAY
    erinn_hour = erinn_today_ms // ERINN_TIME_PER_HOUR
    erinn_minute = erinn_today_ms % ERINN_TIME_PER_HOUR // ERINN_TIME_PER_MIN // 10 * 10
    erinn_now = server_now.replace(hour=erinn_hour, minute=erinn_minute) + datetime.timedelta(minutes=10)
    time_str = datetime.datetime.strftime(erinn_now, "%H:%M %p") 
    return time_str

async def update_clock_on_channel_name(bot: Bot):
    erinn_time = await get_erinn_time()
    server_time = await get_server_time()
    local_time = await get_local_time()
    tokyo_time = await get_tokyo_time()
    
    await update_channel_name_by_bot(bot, ERINN_TIME_CHANNEL_ID, f"爱琳时间：　　{erinn_time}")
    await update_channel_name_by_bot(bot, SERVER_TIME_CHANNEL_ID, f"服务器时间：　{server_time}")
    for this_channel in LOCAL_TIME_CHANNEL_ID_LIST:
        await update_channel_name_by_bot(bot, this_channel, f"北京时间：　　{local_time}")
    for this_channel in TOKYO_TIME_CHANNEL_ID_LIST:
        await update_channel_name_by_bot(bot, this_channel, f"东京时间：　　{tokyo_time}")


if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()

    loop.run_until_complete(get_erinn_time())
