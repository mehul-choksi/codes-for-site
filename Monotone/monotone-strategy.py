#f(x) is a montone, bound is the threshold.		
# lets say we want find the min x such that f(x) >= threshold 
# let domain be [0,inf). For pratical purposes, we'll choose 10^18 as the upper bound	

lo = 0, hi = 10**18 # avoid going over 1e18 if using cpp/java, else you'll run into an overflow 

ans = -1

while lo <= hi:
	mid = lo + hi

	if f(mid) >= threshold:
		ans = min(ans,mid)
		# because f(x) is a monotone, if f(x) >= bound, then f(x+k) >= bound for all k >= 0
		# but we are trying to search the minimum, hence, we can discard the domain [x+1, hi].
		# Lets focus on domain [0, x-1]

		hi = mid-1
	else:	
		# curr f(mid) doesnt not satisfy the constraints
		# because f(x) is a monotone, we can argue that f(x-k) will never satisfy the constraints (where k is some positive constant)
		# Hence we discard range [lo, x]
		lo = mid+1
#print(ans)
