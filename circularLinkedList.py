class node:
	def __init__(self,value = None):
		self.value = value 
		self.next = None 

class circularLinkedList:
	def __init__(self):
		self.root = None 
		self.size = 0

	def insert(self,value):
		if self.size == 0:
			self.root = node(value)
			self.root.next = self.root 
		else:
			newNode = node(value)
			curNode = self.root 
			while curNode.next != self.root:
				curNode = curNode.next
			curNode.next = newNode 
			newNode.next = self.root
		self.size += 1

	def search(self,value):
		curNode = self.root 
		while True:
			if value == curNode.value:
				return True
			if curNode.next == self.root:
				return False 
			curNode = curNode.next 

	def printList(self):
		if self.root == None:
			return 
		curNode = self.root
		print(curNode.value) 
		while curNode.next != self.root:
			curNode = curNode.next 
			print(curNode.value)

	def delete(self,value):
		curNode = self.root 
		prevNode = None 
		while True:
			if curNode.value == value:
				if prevNode != None:
					prevNode.next = curNode.next
				else:
					while curNode.next != self.root:
						curNode = curNode.next
					curNode.next = self.root.next
					self.root = self.root.next
				self.size -= 1
				return True
			elif curNode.next == self.root:
				return False 
			prevNode = curNode
			curNode = curNode.next


#Driver code for Circular Linked list
#Uncomment to test
"""
mL = circularLinkedList()
mL.insert(1)
mL.insert(2)
mL.insert(3)
mL.insert(4)
mL.insert(5)
mL.insert(6)
mL.printList()
print("\n")
	mL.delete(4)
mL.printList()
print("\n")
print(mL.search(4))
print(mL.search(7))
print("\n")
print(mL.root.value)
"""

