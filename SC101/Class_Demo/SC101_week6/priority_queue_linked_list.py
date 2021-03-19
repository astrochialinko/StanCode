"""
File: priority_queue_linked_list.py
Name: 
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
				pass
			else:
				# New node in between
				pass
				# New node at the end
				pass


if __name__ == '__main__':
	main()
