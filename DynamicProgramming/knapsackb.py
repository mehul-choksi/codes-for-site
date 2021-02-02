N,W = map(int,input().split())
v,w = [0]*N, [0]*N
for i in range(N):
	w[i],v[i] = map(int,input().split())
val = sum(v)
dp = [[float('inf') for x in range(val+1)] for i in range(N)]
dp[0][0] = 0
dp[0][v[0]] = w[0]
for i in range(1,N):
	for j in range(val+1):
		if j >= v[i]:
			dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]] + w[i])
		else:
			dp[i][j] = min(dp[i][j], dp[i-1][j])
ans = 0
for i in range(val+1):
	if dp[N-1][i] <= W:
		ans = i
print(ans)
