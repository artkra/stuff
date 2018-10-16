import asyncio

async def sleepnprint(time):
    await asyncio.sleep(time)
    print('Hello after {} seconds'.format(time))


ioloop = asyncio.get_event_loop()

tasks = [ioloop.create_task(sleepnprint(10 - i)) for i in range(10)]

try:
    ioloop.run_until_complete(asyncio.wait(tasks))
except:
    pass
finally:
    ioloop.close()
