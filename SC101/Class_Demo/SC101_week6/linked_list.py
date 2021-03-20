"""
File: linked_list.py
Name: Chia-Lin Ko
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""

class ListNode:
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next


def main():
	node1 = ListNode(val=('A', 3), next=None)  # node1 = oXA21
	node3 = ListNode(('C', 7), None)
	node2 = ListNode(('B', 5), node3)

	node1.next = node2
	linked_list = node1

	traversal(linked_list)


def traversal(linked_list):
	cur = linked_list

	# method 1
	while cur.next is not None:
		print(cur.val)
		cur = cur.next
	print(cur.val)

	# method 2
	# while cur is not None:
	# 	print(cur.val)
	# 	cur = cur.next








if __name__ == '__main__':
	main()
