"""
File: tree.py
Name: Chia-Lin Ko
-------------------------
This file shows the basic concepts for binary trees.
After constructing a tree, we will do 3 traversal examples:
Pre-order
In-order 
Post-order
"""

class Tree:
	def __init__(self, left, val, right):
		self.left = left
		self.val = val
		self.right = right


def main():
	leaf1 = Tree(None, 2, None)
	leaf2 = Tree(None, 6, None)
	leaf3 = Tree(None, 18, None)
	leaf4 = Tree(None, 40, None)

	node1 = Tree(leaf1, 4, leaf2)
	node2 = Tree(leaf3, 19, leaf4)

	root = Tree(node1, 17, node2)

	pre_order(root)
	print('pre-order')
	in_order(root)
	print('in_order')
	post_order(root)
	print('post-order')
	bfs(root)
	print('bfs')


def pre_order(root):
	if root is None:
		pass
	else:
		print(root.val, end=' ')
		pre_order(root.left)
		pre_order(root.right)


def in_order(root):
	if root is None:
		pass
	else:
		in_order(root.left)
		print(root.val, end=' ')
		in_order(root.right)


def post_order(root):
	if root is None:
		pass
	else:
		post_order(root.left)
		post_order(root.right)
		print(root.val, end=' ')


def bfs(root):
	queue = [root]
	while len(queue) != 0:
		node = queue.pop(0)
		print(node.val, end=' ')
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)


if __name__ == '__main__':
	main()
