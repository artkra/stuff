def calc():
    while True:    	
    	z = (yield) 
    	print z.upper()

def main():
	c = calc()
	c.next()
	while True:
		c.send(raw_input('type to echo ->  '))

if __name__ == '__main__':
	main()
