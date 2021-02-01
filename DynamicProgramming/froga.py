n = int(input())
h = [int(x) for x in input().split()]

dp = [0 for i in range(n)]
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
	dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
print(dp[-1])
