#Compare Merge Sort and Quick sort algorithms here. 
def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2 
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			#Less than or less than equal to
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		#Check for any element left behind 
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
		
def quickSort(arr):
	if len(arr) <= 1:
		return arr 
	pivot = arr[randint(0,len(arr) - 1)]
	smaller = []; equal = []; larger = []
	for x in arr:
		if x < pivot:
			smaller.append(x)
		elif x == pivot:
			equal.append(x)
		else:
			larger.append(x)
	return quickSort(smaller) + equal + quickSort(larger)


#Driver code for sorting 
#Uncomment to test
"""
from time import time 
from random import randint,shuffle
arr = [i for i in range(1,21)]
arr = sorted(arr,reverse = True)
t1 = time()
mergeSort(arr)
mergeTime = time() - t1
print("Time taken for Merge sorting:")
print(mergeTime)
print(arr)
print("\n")

arr = sorted(arr,reverse = True)
t1 = time()
a = quickSort(arr)
quickTime = time() - t1
print("Time taken for Quick sorting:")
print(quickTime)
print(a)
"""
