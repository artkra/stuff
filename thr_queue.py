from threading import Thread
from queue import Queue
import time


queue = Queue()

def producer():
	global queue

	while True:
		time.sleep(1)
		queue.put(1)
		print('PUT 1')

def consumer():
	global queue

	while True:
		item = queue.get()
		print('GOT {} FROM QUEUE'.format(item))
		queue.task_done()


if __name__ == '__main__':
	t1 = Thread(target=producer)
	t2 = Thread(target=consumer)

	t1.start()
	t2.start()

	t1.join()
	t2.join()