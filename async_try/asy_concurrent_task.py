
import asyncio


async def task_func():
    print('in task_func\n\n')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print('waiting for {!r}\n\n'.format(task))
    return_value = await task
    task_to_cancel = loop.create_task(task_func())
    task_to_cancel.cancel()
    print('task completed {!r}'.format(task))
    print('\n\nreturn value: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()