class E(object):
	def __init__(self, value, next = None):
		self.value = value 
		self.next = next 

def print_lili(e):
	print(e.value)
	if e.next:
		print_lili(e.next)

def rev(head):
	cur = head
	next = head.next
	while next:
	  tmp = next.next
	  next.next = cur
	  cur = next
	  next = tmp
	head.next = None
	return cur


def main():
	lili = E(1, E(2, E(3, E(4))))
	print('Default list\n')
	print_lili(lili)
	print('\nReversed list\n')
	print_lili(rev(lili))
	

if __name__ == '__main__':
	main()