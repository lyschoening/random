import asyncio
import random
from aiohttp import web

RANDOM_NUMBER = random.randint(1, 100)


def random(request):
    return web.Response(text="Your random number: {n}".format(n=RANDOM_NUMBER))


app = web.Application()
app.router.add_route('GET', '/', random)

web.run_app(app, port=5000)
