import time

class E(object):
	def __init__(self, value, next = None):
		self.value = value 
		self.next = next 

def mll(a):
	for i in a:
		while True:
			
	

def print_lili(e):	
	if e.next:
		print_lili(e.next)
	print(e.value)


def main():
	a = [1, 2, 3, 4, 5, 6, 7]
	lili = E(1, E(2, E(3, E(4))))
	print_lili(mll(a))


if __name__ == '__main__':
	main()