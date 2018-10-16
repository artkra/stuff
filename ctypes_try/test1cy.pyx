cdef printer():
	for _ in range(10000):
		print(_repr_("hello"))
cdef main():
	printer()

if __name__ =='__main__':
	main()