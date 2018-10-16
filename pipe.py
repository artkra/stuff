from multiprocessing import Pipe 
import time

def main():
	op, ip = Pipe()
	for _ in range(9):
		ip.send('ping?pong')
	time.sleep(0.1)
	for _ in range(10):
		print op.recv()

if __name__ == '__main__':
	main()