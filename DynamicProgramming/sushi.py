n = int(input())
count = [0] * 4
t = input().split()
for i in t:
	count[int(i)]+= 1

dp = [[[-1 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]

# state dp[x][y][z] = expected count for x 3's, y 2's, z 1's. Number of zeroes = n - (x+y+z)

# transition: from each state we can go to a different state by picking a plate of 3 or 2 or 1 or 0

# dp[x][y][z] = 1 + p3 * dp[x-1][y+1][z] + p2 * dp[x][y-1][z+1] + p1 * dp[x][y][z-1] + p0 * dp[x][y][z]
 
# one is added because no matter what the outcome, a move will always be made on dp[x][y][z]. p1,p2,p3,p0 are probabilities of choosing plates with 1,2,3 and 0 sushis respectively.

# because the term with p0 has dp[x][y][z], it can be transposed to right hand side. The equation then becomes:

# dp[x][y][z] -  p0 * dp[x][y][z] = 1 + p3 * dp[x-1][y+1][z] + p2 * dp[x][y-1][z+1] + p1 * dp[x][y][z-1]
# or dp[x][y][z] * (1-p0) = 1 + p3 * dp[x-1][y+1][z] + p2 * dp[x][y-1][z+1] + p1 * dp[x][y][z-1]
# or dp[x][y][z] = (1 + p3 * dp[x-1][y+1][z] + p2 * dp[x][y-1][z+1] + p1 * dp[x][y][z-1])/(1-p0)

dp[0][0][0] = 0

# ordering is important. The outer most loop should be iterating on the state 3, followed by 2, followed by 1
# reason: Transitions using the state of 3 sushi's requires the value of the problem having one more 2 sushi plates. In other words, state of 3 plates is dependent of state of 2 plate
# similarly state of 2 plates is dependent on state of 1 plate.
 
for i in range(n+1):
	for j in range(n+1):
		for k in range(n+1):
			z = n - (i+j+k)
			if i+j+k > n or z == n:
				continue
			val = 1
			if i > 0:
				val += (i/n) * dp[i-1][j+1][k]
			if j > 0:
				val += (j/n) * dp[i][j-1][k+1]
			if k > 0:
				val += (k/n) * dp[i][j][k-1]

			val /= (1-(z/n))

			dp[i][j][k] = val

print(dp[count[3]][count[2]][count[1]])
