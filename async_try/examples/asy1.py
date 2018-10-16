import asyncio
import aiohttp

async def foo():
    print('running in foo')
    await asyncio.sleep(1)
    print('done in foo')

async def bar():
    print('running in bar')
    await foo()
    print('done in bar')


ioloop  = asyncio.get_event_loop()

# tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]

tasks = [ioloop.create_task(bar())]

wait_tasks = asyncio.wait(tasks)

ioloop.run_until_complete(wait_tasks)

ioloop.close()



