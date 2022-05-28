from khl import Message


async def update_channel_name(msg: Message, channel_id: str, new_name: str):
    method = "POST"
    route = "channel/update"
    json = {
        "channel_id": channel_id,
        "name": new_name,
    }

    await msg.ctx.gate.request(method=method, route=round, json=json)    
