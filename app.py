import asyncio

from aiohttp import web
from aiozmq import rpc

async def hello(request):
    client = await rpc.connect_rpc(connect='tcp://worker:5555')

    sentence = await client.call.make_a_sentence('Hello', 'world')
    return web.Response(text=sentence)


app = web.Application()
app.router.add_route('GET', '/', hello)
web.run_app(app)
