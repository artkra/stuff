import random

syms = [' ', ' ', 'a', 'b']

s = ''.join([random.choice(syms) for _ in range(200)])

def one_spacer(s):
	res = ''
	spaces = 0

	i = 0

	while i < len(s) - 1:
		if spaces == 0:
			res += s[i]
			if s[i] == ' ':
				spaces += 1
		else:
			if s[i] != ' ':
				res += s[i]
				spaces = 0

		i += 1

	return res


if __name__ == '__main__':
	print(s)
	print('----------------------')
	print(one_spacer(s))