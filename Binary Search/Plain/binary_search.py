def binary_search(a,key):
	lo,hi,mid = 0, len(a)-1, 0
	
	while lo <= hi:
		mid = int((lo + hi)/2)
		
		if a[mid] > key:	# Discard right half if current element > key
			hi = mid-1
		elif a[mid] < key:	# Discard left half if current element < key
			lo = mid+1
		else:				# Element found
			return mid

	return -1 #Not found

if __name__ == "__main__":
	a = [1,2,3,4,5,6,7,8]
	loc = binary_search(a,3)

	if loc != -1:
		print("Found element at: ", loc)
	else:
		print("Did not find element")
