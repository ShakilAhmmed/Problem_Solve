def printLinkedList(head):
	if head is not None:
		print(head.data)
		printLinkedList(head.next)
