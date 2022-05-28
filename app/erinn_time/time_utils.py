import datetime

# from utils.channel_utils import update_channel_name


ERINN_TIME_PER_MIN = 1500   # ms
ERINN_TIME_PER_HOUR = 60 * ERINN_TIME_PER_MIN
ERINN_TIME_PER_DAY = 24 * ERINN_TIME_PER_HOUR


async def get_local_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
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
    erinn_minute = erinn_today_ms % ERINN_TIME_PER_HOUR // ERINN_TIME_PER_MIN
    erinn_now = server_now.replace(hour=erinn_hour, minute=erinn_minute)
    time_str = datetime.datetime.strftime(erinn_now, "%H:%M %p") 
    return time_str


if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()

    loop.run_until_complete(get_erinn_time())
