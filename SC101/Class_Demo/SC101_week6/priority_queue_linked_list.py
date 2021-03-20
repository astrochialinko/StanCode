"""
File: priority_queue_linked_list.py
Name: Chia-Lin Ko
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It controls the condition to break the input loop
EXIT = ''


class ListNode:
	def __init__(self, val, next_one):
		self.val = val
		self.next = next_one


def main():
	priority_queue = None
	while True:
		name = input(f'Name of patient ({EXIT} to quit): ')
		if name == EXIT:
			break
		priority = int(input('Priority: '))
		data = (name, priority)
		if priority_queue is None:
			priority_queue = ListNode(data, None)
		else:
			if priority_queue.val[1] > priority:
				# New node at the beginning
				node = ListNode(data, priority_queue)
				#node = ListNode(data, None)
				#node.next = priority_queue
				priority_queue = node
			else:
				cur = priority_queue
				# New node in between
				while cur.next is not None:
					if cur.val[1] <= priority < cur.next.val[1]:
						node = ListNode(data, None)
						node.next = cur.next
						cur.next = node
						break
					cur = cur.next
				# New node at the end
				if cur.next is None:
					node = ListNode(data, None)
					cur.next = node

	print('--------------------------------')
	traversal(priority_queue)


def traversal(linked_list):
	cur = linked_list
	while cur.next is not None:
		print(cur.val)
		cur = cur.next
	print(cur.val)

if __name__ == '__main__':
	main()
