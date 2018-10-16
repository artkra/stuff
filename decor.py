def main():
	show()

def bitch_decorator(f):
	def wrapped():
		print 'HELLO, BITCH!'
		f()
	return wrapped

@bitch_decorator
def show():
	print 'IT\'s SHOW TIME!'

if __name__ == '__main__':
	main()