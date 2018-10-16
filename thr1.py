import threading
import time

def foo(i):
	time.sleep(i/10)
	print(threading.currentThread().getName())

def go():
	for i in range(10):
		t = threading.Thread(target=foo, args=(i,))
		t.start()

def go_go():
	for i in range(10):
		t = threading.Thread(target=foo, args=(i,))
		t.start()
		t.join()

		
if __name__ == '__main__':
	try:
		go()
		print('goodbye')
	except KeyboardInterrupt:
		pass