import threading, time, Queue

def f(x):
	print x 

def main():
	l = threading.Lock()
	for i in range(10):
		i += 1
		t = threading.Thread(target = f, args = (str('<>'*i), ))
		t.start()
		time.sleep(0.1)
		l.acquire()
		print '-->'
		l.release()
		t.join()
	for i in range(100):
		q = Queue.Queue()
		q.put(i)
		tq = threading.Thread(target = f, args = (q.get(), ))
		tq.start()

if __name__ == '__main__':
	main()