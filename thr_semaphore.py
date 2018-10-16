import threading
import time
import random

item = 0

semaphore = threading.Semaphore(0)

def consumer():
	print('consumer is waiting')
	semaphore.acquire()
	print('consumer notify: consumed item number %s ' % item)

def producer():
	global item
	time.sleep(1)
	item = random.randint(0, 1000)
	print('producer notify: produced item number %s ' % item)
	semaphore.release()


if __name__ == '__main__':
	for _ in range(5):
		t1 = threading.Thread(target=producer)
		t2 = threading.Thread(target=consumer)
		t1.start()
		t2.start()
		t1.join()
		t2.join()
	print('STOP')