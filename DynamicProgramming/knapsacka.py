N,W = map(int,input().split())
w,v = [0]*N, [0]*N

for i in range(N):
	w[i],v[i] = map(int,input().split())

dp = [[0 for j in range(W+1)] for i in range(N)]

for i in range(N):
	for j in range(W+1):
		if j >= w[i]:
			dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
		else:
			dp[i][j] = dp[i-1][j]
print(dp[N-1][W])
