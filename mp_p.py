import multiprocessing as mp
import time

def foo(i):
	print('task {} started'.format(i))
	time.sleep(2)
	print('task {} finished'.format(i))


if __name__ == '__main__':
	tasks = []
	for i in range(5):
		p = mp.Process(target=foo, args=(i,))
		tasks.append(p)
		p.start()
	
	for task in tasks:
		task.join()	

	print('ALL DONE')