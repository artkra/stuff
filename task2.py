from time import sleep

a = [0 for _ in range(5)]

def set_next(arr, set):
	argument = 1 if set else 0
	arr[arr.index(1) + 1] = argument

def set_first(arr, set):
	argument = 1 if set else 0
	arr[0] = argument

def fill_desk(arr, set1, set2):
	if sum(arr) < len(arr):	

		set_first(arr, set1)
		print(arr)
		sleep(0.1)

		if arr.index(1) + 1 < len(arr):
			if arr[arr.index(1) + 1] == 0:
				set2 = True
			else:
				set2 = False

			set_next(arr, set2)
			print(arr)
			sleep(0.1)
		
		fill_desk(arr, not set1, set2)

fill_desk(a, True, True)