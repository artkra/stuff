import asyncio

async def outer():
	print('outer coroutine')
	res1 = await phase1()
	res2 = await phase2()
	return '{} - {}'.format(res1, res2)

async def phase1():
	return 'this'

async def phase2():
	return 'that'

event_loop = asyncio.get_event_loop()

try:
	print(event_loop.run_until_complete(outer()))
finally:
	print('that\'s it')
	event_loop.close()
