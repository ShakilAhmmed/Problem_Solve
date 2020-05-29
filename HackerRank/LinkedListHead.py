class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SinglyLinkedList:
	def __init__(self):
		self.head = None


def insertNodeAtHead(llist, data):
	new = Node(data)
	if llist == None:
		llist = new
	else:
		new.next = llist
		llist = new
	return llist
