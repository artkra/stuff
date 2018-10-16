from random import randint

class BinaryNode(object):
	"""docstring for BinaryNode"""
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def add(self, val):
		if val <= self.value:
			if self.left:
				self.left.add(val)
			else:
				self.left = BinaryNode(val)

		else:
			if self.right:
				self.right.add(val)
			else:
				self.right = BinaryNode(val)
		


class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		self.root = None

	def add(self, value):
		if self.root is None:
			self.root = BinaryNode(value)
		else:
			self.root.add(value)

	def __contains__(self, target):
		node = self.root
		while node:
			if target < node.value:
				node = node.left
			elif target > node.value:
				node = node.right
			else:
				return True

		return node is not None


if __name__ == '__main__':
	BTS = BinaryTree()

	vals = [randint(1, 100) for _ in range(50)]

	for i in vals:
		BTS.add(i)

	for i in vals:
		print(i in BTS)
		