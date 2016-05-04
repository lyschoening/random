import asyncio
from random import randint

from aiozmq import rpc

WORKER_ID = randint(1, 100)

class WorkerHandler(rpc.AttrHandler):
    @rpc.method
    def make_a_sentence(self, greeting: str, subject: str) -> str:
        return '[Worker {} says]: {}, {}!'.format(WORKER_ID, greeting, subject)


async def worker():
    await rpc.serve_rpc(WorkerHandler(), bind='tcp://0.0.0.0:5555')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(worker())
    loop.run_forever()
