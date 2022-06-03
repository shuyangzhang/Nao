import datetime
from http import server
from urllib import response
import aiohttp
import json
from app.daily_mission.i18n import ZH_CN, KR_TO_ZH_CN

MABI_WIKI_URL = "https://mabi.world/sm/mww/{}/{}/{}.json"
SIGKILL_URL = "https://mabi-api.sigkill.kr/get_todayshadowmission"

async def get_server_time():
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=4) - datetime.timedelta(hours=7)
    return now

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def daily_mission_from_mabiwiki():
    server_time = await get_server_time()
    year, month, day = server_time.year, server_time.month, server_time.day
    url = MABI_WIKI_URL.format(year, month, day)
    async with aiohttp.ClientSession() as session:
        response = json.loads(await fetch(session, url))
    taillteann = response["Taillteann"]["Normal"]
    tara = response["Tara"]["Normal"]
    taillteann = ZH_CN[taillteann]
    tara = ZH_CN[tara]
    return f"塔汀:{taillteann} , 塔拉:{tara}"

async def daily_mission_from_sigkill():
    server_time = await get_server_time()
    year, month, day = server_time.year, server_time.month, server_time.day
    url = f"{SIGKILL_URL}/{year}-{month}-{day}"
    async with aiohttp.ClientSession() as session:
        response = json.loads(await fetch(session, url))
    taillteann = response["Taillteann"]["normal"]["name"]
    tara = response["Tara"]["normal"]["name"]
    taillteann = KR_TO_ZH_CN[taillteann]
    tara = KR_TO_ZH_CN[tara]
    return f"塔汀:{taillteann} , 塔拉:{tara}"
