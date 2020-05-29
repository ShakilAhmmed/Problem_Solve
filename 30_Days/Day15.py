class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Solution:
	def display(self, head):
		current = head
		while current:
			print(current.data, end = ' ')
			current = current.next

	def insert(self, head, data):
		if head is None:
			head = Node(data)
		elif head.next is None:
			head.next = Node(data)
		else:
			self.insert(head.next, data)
		return head


# Complete this method


mylist = Solution()
