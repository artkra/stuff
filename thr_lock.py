import threading
import time

RESULT = 0
TIMES = 1000000

lock = threading.Lock()

class Timer(object):
	def __init__(self):
		self.start = time.time()

	def __enter__(self):
		pass

	def __exit__(self, a, b, c):
		end = time.time()
		print(end - self.start, ' s')

def incr():
	global RESULT, lock

	for _ in range(TIMES):
		lock.acquire()
		print(threading.currentThread().getName())
		RESULT += 1
		lock.release()

def decr():
	global RESULT, lock

	for _ in range(TIMES):
		lock.acquire()
		print(threading.currentThread().getName())
		RESULT -= 1
		lock.release()

if __name__ == '__main__':

	with Timer() as timer:	
		t1 = threading.Thread(target=incr)
		t2 = threading.Thread(target=decr)
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		print(RESULT)