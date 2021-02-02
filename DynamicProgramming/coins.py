n = int(input())
p = list(map(float,input().split()))

if n == 1:
	print(p[0])
	exit()

dp = [[0 for x in range(n+1)] for i in range(n)]

dp[0][0],dp[0][1] = 1-p[0], p[0]

for i in range(1,n):
	dp[i][0] = dp[i-1][0] * (1 - p[i])


for i in range(1,n):
	for j in range(1,n+1):
		dp[i][j] = p[i] * dp[i-1][j-1] + (1-p[i]) * dp[i-1][j]

ans, thres = 0, n//2 + 1
for i in range(thres,n+1):
	ans += dp[-1][i]

print(ans)
