import datetime
import aiohttp
import json
from app.daily_mission.i18n import ZH_CN

URL = "https://mabi.world/sm/mww/{}/{}/{}.json"

async def get_server_time():
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=4) - datetime.timedelta(hours=7)
    return now

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def daily_mission():
    server_time = await get_server_time()
    year, month, day = server_time.year, server_time.month, server_time.day
    url = URL.format(year, month, day)
    async with aiohttp.ClientSession() as session:
        response = json.loads(await fetch(session, url))
    taillteann = response["Taillteann"]["Normal"]
    tara = response["Tara"]["Normal"]
    taillteann = ZH_CN[taillteann]
    tara = ZH_CN[tara]
    return f"塔汀:{taillteann} , 塔拉:{tara}"
