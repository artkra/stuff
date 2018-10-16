from Queue import Queue
from threading import Thread
from time import sleep

def pr(x):
	print x

def addtoq(q):
	q.put('-><-')
	sleep(0.1)

def main():
	q = Queue()
	while True:
		addtoq(q)
		try:
			item = q.get_nowait()
			t = Thread(target = pr, args = (item, ))
			t.start()
			t.join()
		except Queue.empty, error:
			continue

if __name__ == '__main__':
	main()