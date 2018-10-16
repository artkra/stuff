import multiprocessing as mp 
import time

def f():
	for i in xrange(100000
		0):
		s = i*i*i

def main():
	p = mp.Pool(10)
	start = time.time()
	p.map(f, [])
	print time.time() - start 
	start = time.time()
	f()
	print time.time() - start 

if __name__ == '__main__':
	main()