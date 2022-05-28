from khl import Message, Bot


async def update_channel_name_by_message(msg: Message, channel_id: str, new_name: str):
    method = "POST"
    route = "channel/update"
    json = {
        "channel_id": channel_id,
        "name": new_name,
    }

    await msg.ctx.gate.request(method=method, route=route, json=json)    

async def update_channel_name_by_bot(bot: Bot, channel_id: str, new_name: str):
    method = "POST"
    route = "channel/update"
    json = {
        "channel_id": channel_id,
        "name": new_name,
    }

    await bot.client.gate.request(method=method, route=route, json=json)    
