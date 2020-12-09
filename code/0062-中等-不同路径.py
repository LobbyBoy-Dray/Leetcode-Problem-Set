def uniquePaths(m, n):
    tmp = [None] * n 
    dp  = [tmp.copy() for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if row == 0:
                dp[row][col] = 1
            elif col == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-1][col]+dp[row][col-1]
    return dp[-1][-1]


if __name__ == "__main__":
    test1 = uniquePaths(7,3)
    print(test1)