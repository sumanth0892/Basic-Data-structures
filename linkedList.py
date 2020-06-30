class node:
	def __init__(self,value = None):
		self.value = value 
		self.next = None 

class linkedList:
	def __init__(self):
		self.root = node()

	def insert(self,value):
		curNode = self.root 
		while curNode.next != None:
			curNode = curNode.next 
		curNode.next = node(value)

	def getSize(self):
		#gets the length of the list
		size = 0
		curNode = self.root
		while curNode.next != None:
			curNode = curNode.next
			size += 1
		return size 

	def printList(self):
		#Prints the elements of the list 
		elements = []
		curNode = self.root 
		while curNode.next != None:
			curNode = curNode.next 
			elements.append(curNode.value)
		print(elements)

	def getValue(self,index):
		#Get a value at a particular index 
		if index >= self.getSize():
			print("Index out of range!")
			return False
		curIdx = 0
		curNode = self.root 
		while True:
			curNode = curNode.next 
			if index == curIdx:
				return curNode.value 
			curIdx += 1

	def search(self,value):
		curIdx = 0
		curNode = self.root
		while True:
			if curIdx >= self.getSize():
				return False 
			curNode = curNode.next 
			if value == curNode.value:
				return True 
			curIdx += 1

	def delete(self,index):
		if index >= self.getSize():
			print("Index out of range!")
			return False 
		curIdx = 0
		curNode = self.root
		print("List before deleting value:")
		self.printList()
		while True:
			nextNode = curNode
			curNode = curNode.next 
			if index == curIdx:
				nextNode.next = curNode.next
				self.printList()
				return True 
			curIdx += 1


#Driver code for Linked list 
#Uncomment to test
""" 
L = linkedList()
L.insert(1)
L.insert(2)
L.insert(3)
L.insert(-0.5)
L.insert(4)
L.insert(-1)
print(L.getSize())
print(L.search(1))
print(L.search(5))
L.delete(1)
L.delete(6)
"""























