import asyncio

from aiohttp import web
from aiozmq import rpc

client = None

async def hello(request):
    sentence = await client.call.make_a_sentence('Hello', 'world')
    return web.Response(text=sentence)

app = web.Application()
app.router.add_route('GET', '/', hello)


async def server(loop):
    global client
    client = await rpc.connect_rpc(connect='tcp://worker:5555')
    await loop.create_server(app.make_handler(), '0.0.0.0', 8080)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server(loop))
    loop.run_forever()
