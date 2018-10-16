import math

given = [x if x != 17 and x != 5 else 0 for x in range(100)]

normal = [x for x in range(100)]

def sq_eq(a, b, c):
	D = b*b - 4*a*c 
	x1 = (-b + math.sqrt(D)) / (2 * a)
	x2 = (-b - math.sqrt(D)) / (2 * a)
	return (int(x1), int(x2))

def main():
	print(given)
	print('\n\n')
	print(normal)
	print('\n\nDifference: ' + str(sum(normal) - sum(given)))
	sq_given = [x*x for x in given]
	sq_normal = [x*x for x in normal]
	print('\n\nSquared given:' + str(sum(sq_given)))
	print('\n\nSquared normal:' + str(sum(sq_normal)))
	print('\n\nSquared diff:' + str(sum(sq_normal) - sum(sq_given)))
	A = sum(normal) - sum(given)
	B = sum(sq_normal) - sum(sq_given)
	print('x + y = ' + str(A) + '\n')
	print('x^2 + y^2 = ' + str(B) + '\n')
	a = 2
	b = 2*A
	c = A*A - B
	print('=> 2x^2 - ' + str(b) + ' x + ' + str(c) + ' = 0')
	print('\n\n Missing values are: ' + str(sq_eq(a, -b, c)))


if __name__ == '__main__':
	main()