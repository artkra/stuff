import random

arr = [random.randint(0,1) for _ in range(100)]

def count_max(arr):
	sizes = []
	this_size = 0
	zeros = 0
	max_count = 0

	for i in arr:
		if i == 1:
			this_size += 1
			zeros = 0
		elif i == 0 and zeros == 0:
			sizes.append(this_size)
			this_size = 0
			zeros += 1
		elif i == 0 and zeros > 0:
			sizes.append(0)

	j = 0

	while j < len(sizes)-1:
		summ = sizes[j] + sizes[j+1]
		if summ > max_count:
			max_count = summ
		j += 1

	return sizes, max_count


if __name__ == '__main__':
	print(arr)
	print('\n')
	print(count_max(arr))