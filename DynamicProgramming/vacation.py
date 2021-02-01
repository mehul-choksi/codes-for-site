n = int(input())
arr = [[0 for i in range(n)] for x in range(3)]
for i in range(n):
	temp = list(map(int,input().split()))
	arr[0][i],arr[1][i],arr[2][i] = temp[0],temp[1],temp[2]

dp = [[0 for x in range(n)] for i in range(3)]
dp[0][0],dp[1][0],dp[2][0] = arr[0][0], arr[1][0], arr[2][0]

for i in range(1,n):
	dp[0][i] = max(dp[1][i-1],dp[2][i-1]) + arr[0][i] 
	dp[1][i] = max(dp[0][i-1],dp[2][i-1]) + arr[1][i]
	dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + arr[2][i]

print(max(dp[0][n-1],dp[1][n-1],dp[2][n-1]))
