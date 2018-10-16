import threading as thr
import time

event = thr.Event()

def producer(event):
	while True:
		time.sleep(2)
		print('EVENT SET!')
		event.set()
		event.clear()

def consumer(event):
	while True:
		time.sleep(2)
		event.wait()
		print('GOT AN EVENT!')

if __name__ == '__main__':
	t1 = thr.Thread(target=producer, args=(event,))
	t2 = thr.Thread(target=consumer, args=(event,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()