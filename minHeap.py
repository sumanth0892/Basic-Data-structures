#List-based implementation of a Min Heap
#Uses a binary tree structure. 
#The parent of any node i is at i//2
#The child is at either i*2 or i*2 + 1
class minHeap:
	def __init__(self):
		self.values = None 
		self.size = 0

	def buildHeap(self,values):
		i = len(values)//2
		self.size = len(values)
		self.values = [0] + values[:]
		while i > 0:
			self.bubbleDown(i)
			i -= 1

	def bubbleDown(self,i):
		while (i*2) <= self.size:
			mc = self.minChild(i)
			if self.values[i] > self.values[mc]:
				self.values[i],self.values[mc] = self.values[mc],self.values[i]
			i = mc 

	def minChild(self,i):
		if i*2 + 1 > self.size:
			return i*2
		else:
			if self.values[i*2] < self.values[i*2 + 1]:
				return i*2
			else:
				return i*2 + 1

	def deleteMin(self):
		retVal = self.values[1]
		self.values[1] = self.values[self.size]
		self.size -= 1
		self.values.pop()
		self.bubbleDown(1)
		return retVal 

#Driver code for Heap - Min and Max
#Uncomment to test 
"""
bh = minHeap()
bh.buildHeap([9,5,6,2,3])
print(bh.deleteMin())
print(bh.deleteMin())
print(bh.deleteMin())
print(bh.deleteMin())
print(bh.deleteMin())
"""
