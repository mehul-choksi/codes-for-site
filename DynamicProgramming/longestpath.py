import sys
sys.setrecursionlimit(10**6)

def memo_dfs(g,v,dp):
	max_depth = 0
	if dp[v] != -1:
		return dp[v]

	for nei in g[v]:
		max_depth = max(max_depth,memo_dfs(g,nei,dp))

	dp[v] = max_depth + 1

	return dp[v]
n,m = map(int,input().split())
g = [[] for i in range(n+1)]

for i in range(m):
	a,b = map(int,input().split())
	g[a].append(b)

dp = [-1] * (n+1)

for i in range(1,n+1):
	memo_dfs(g,i,dp)

print(max(dp)-1)
