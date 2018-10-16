import threading, time

def print_some():
	time.sleep(1)
	print 'some ==>'

def wait_n_print():
	time.sleep(2)
	print '(.)(.)'

def main():
	for _ in range(10):
		t1 = threading.Thread(target = print_some)
		t2 = threading.Thread(target = wait_n_print)
		t1.start()
		t2.start()
	t1.join()
	t2.join()

if __name__ == '__main__':
	main()