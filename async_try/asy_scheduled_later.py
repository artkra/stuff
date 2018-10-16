import asyncio, time 

def callback(n):
	print('some callback shit {}'.format(n))

async def main(loop):
	now = loop.time()
	loop.call_later(0.1, callback, 3)
	loop.call_later(0.2, callback, 2)
	loop.call_later(0.3, callback, 1)
	loop.call_at(now + 0.2, callback, 55)
	print('working')

	await asyncio.sleep(0.5)

event_loop = asyncio.get_event_loop()

try:
	event_loop.run_until_complete(main(event_loop))
	print('done')
finally:
	event_loop.close()