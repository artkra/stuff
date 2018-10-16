import threading
import time

condition = threading.Condition()
item = 0

def producer():
	global condition
	global item

	condition.acquire()
	time.sleep(1)
	item += 1
	print('NOTIFY!')
	condition.notify()
	condition.release()

def consumer():
	global condition
	global item

	condition.acquire()
	while not item:
		condition.wait()
		item -= 0 
	print('I AM NOTIFIED')
	condition.release()

if __name__ == '__main__':
	producer = threading.Thread(target=producer)
	consumer = threading.Thread(target=consumer)

	producer.start()
	consumer.start()

	producer.join()
	consumer.join()



