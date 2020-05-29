class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SinglyLinkedList:
	def __init__(self):
		self.head = None


def insertNodeAtTail(head, data):
	node = Node(data)
	if head is not None:
		head = node
	else:
		current = head
		while current.next:
			current = current.next
		current.next = node
	return head
