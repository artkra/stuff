def fibo(n):
	if n == 0:
		return 0
	elif n <= 2:
		return 1
	else:
		return fibo(n-2) + fibo(n-1)


def num_pali(n):
	rev = ''
	while n//10 > 0:
		rev += str(n%10)
		n = n//10

	rev += str(n%10)

	return int(rev)


def reverse(s):

	if len(s) == 1:
		return s[0]
	else:
		return reverse(s[1:]) + s[0]

def pali(s):
	for i, ch in enumerate(s):
		if s[i] == s[len(s)-1 - i]:
			pass
		else:
			return False
	return True 

if __name__ == '__main__':
	print(pali('adda'))

