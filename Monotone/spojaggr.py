t = int(input())
for tc in range(t):
	n,c = [int(x) for x in input().split()]
	arr = []
	for i in range(n):
		arr.append(int(input()))

	arr.sort()
	lo, hi,ans = 0,10**10,0

	while lo <= hi:
		mid = int((lo + hi)/2)
		count = 1	#first cow will always be included
		prev = arr[0]	
		for i in range(1,n):	
			if arr[i]-prev >= mid:
				count += 1			
				prev = arr[i]
		if count >= c:			
			lo = mid+1
			ans = mid
		else:
			hi = mid-1

	print(ans)
