import asyncio

def mark_done(future, result):
	print('setting future result to {!r}'.format(result))
	future.set_result(result)

event_loop = asyncio.get_event_loop()

try:
	all_done = asyncio.Future()

	event_loop.call_soon(mark_done, all_done, 'RESULTT')

	result = event_loop.run_until_complete(all_done)
finally:
	print('DONE!')
	event_loop.close()
	print('future result is {!r}'.format(all_done.result()))

# async def main(loop):
#     all_done = asyncio.Future()

#     print('scheduling mark_done')
#     loop.call_soon(mark_done, all_done, 'the result')

#     result = await all_done
#     print('returned result: {!r}'.format(result))


# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     event_loop.close()