class Node():
	def __init__(self, val, next):
		self.val = val
		self.next = next

def print_li(node):
	print(node.val)
	if node.next:
		print_li(node.next)

def reverse_li(node):
	cur = node
	nxt = node.next
	while nxt:
		temp = nxt.next
		nxt.next = cur
		cur = nxt
		nxt = temp

	node.next = None
	return cur

# def rev(node):
# 	cur = node
# 	prev = None
# 	while cur:
# 		nxt = cur.next
# 		cur.next = prev
# 		prev = cur
# 		cur = nxt
	
# 	return prev


def rev(node):
	cur = node
	prev = None
	while cur:
		nxt = cur.next
		cur.next = prev
		prev = cur
		cur = nxt
	return prev

if __name__ == '__main__':
	Li = Node(1, Node(2, Node(3, Node(4, None))))

	print_li(Li)
	print(' ')
	# print_li(reverse_li(Li))
	# print(' ')
	# print_li(Li)	
	print_li(rev(Li))