def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
n = 5
print(climb_stairs(n))

#2nd way
def climb_stairs(n):
    # dp[i] = number of ways to reach step i
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way: (1)
    dp[2] = 2  # 2 ways: (1+1), (2)

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 5
print(climb_stairs(n))
