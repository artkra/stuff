import asyncio

async def coroutine():
	print('in coroutine')

event_loop = asyncio.get_event_loop()
try:
	print('starting')
	coro = coroutine()
	print('entering event loop')
	event_loop.run_until_complete(coro)
finally:
	print('stop')
	event_loop.close()
