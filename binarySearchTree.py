class node:
	def __init__(self,value = None):
		self.value = value
		self.left = None 
		self.right = None 
		self.parent = None 

class BST:
	def __init__(self):
		self.root = None 

	def insert(self,value):
		#Add a value to the tree 
		if self.root == None:
			self.root = node(value)
		else:
			#Call a private function to add a value
			self._insert(self.root,value)

	def _insert(self,curNode,value):
		if value == curNode.value:
			print("Value already present!")
		elif value < curNode.value:
			if curNode.left == None:
				curNode.left = node(value)
				curNode.left.parent = curNode 
			else:
				self._insert(curNode.left,value)
		else:
			if curNode.right == None:
				curNode.right = node(value)
				curNode.right.parent = curNode
			else:
				self._insert(curNode.right,value)

	def getHeight(self):
		if self.root == None:
			return 0
		else:
			return self._getHeight(self.root,0)

	def _getHeight(self,curNode,curHeight):
		#Call a private function
		#This can be modified to check whether or not the tree is balanced. 
		#leftHeight == rightHeight
		if curNode == None:
			return curHeight 
		leftHeight = self._getHeight(curNode.left,curHeight + 1)
		rightHeight = self._getHeight(curNode.right,curHeight + 1)
		print("Left Height is:")
		print(leftHeight)
		print("\n")
		print("Right Height is:")
		print(rightHeight)
		return max(leftHeight,rightHeight)

	def printTree(self):
		if self.root == None:
			print("Empty tree!")
		else:
			self._printTree(self.root)

	def _printTree(self,curNode):
		if curNode != None:
			self._printTree(curNode.left)
			print(curNode.value)
			self._printTree(curNode.right)

	def search(self,value):
		if self.root == None:
			return False,None 
		else:
			return self._search(self.root,value)

	def _search(self,curNode,value):
		if value == curNode.value:
			return True, curNode 
		elif value < curNode.value and curNode.left != None:
			return self._search(curNode.left,value)
		elif value > curNode.value and curNode.right != None:
			return self._search(curNode.right,value)
		return False,None 

	def delete(self,value):
		#To delete a value, we need to:
		#1. Determine if the value is in the tree and 
		#2. Find the node where its present 
		status,Node = self.search(value)
		if status:
			self._delete(Node)
		else:
			print("Value not present!")
			return False 

	def _delete(self,Node):
		def getMin(n):
			current = n 
			while current.left != None:
				current = current.left 
			return current 

		def getChildren(n):
			c = 0
			if n.left:
				c += 1
			if n.right:
				c += 1
			return c

		nChildren = getChildren(Node)
		print(nChildren)
		nodeParent = Node.parent 

		if nChildren == 0:
			if nodeParent.left == Node:
				nodeParent.left = None 
			else:
				nodeParent.right = None 

		if nChildren == 1:
			if Node.left != None:
				child = Node.left 
			else:
				child = Node.right 
			if nodeParent.left == Node:
				nodeParent.left = child 
			else:
				nodeParent.right = child 
			child.parent = nodeParent 

		if nChildren == 2:
			successor = getMin(Node.right)
			Node.value = successor.value 
			self._delete(successor)


#Driver code to test binary tree
#Uncomment to test
"""
t = BST()
t.insert(1)
t.insert(2)
t.insert(0)
t.insert(-0.5)
t.insert(3)
t.insert(4)
print(t.getHeight())
t.printTree()
print(t.search(1))
print(t.search(5))
t.delete(5)
t.delete(1)
print("\n")
t.printTree()
"""


























