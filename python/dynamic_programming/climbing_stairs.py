"""LeetCode 70 - Climbing Stairs.

You can climb 1 or 2 steps at a time. How many distinct ways are there to
reach the top of an n-step staircase?

Recurrence: ways(i) = ways(i - 1) + ways(i - 2), the Fibonacci sequence.
"""


def climb_stairs_optimized(n):
    """Keep only the last two values.

    Time: O(n), Space: O(1)
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def climb_stairs_dp(n):
    """Bottom-up DP table.

    dp[i] = number of ways to reach step i.
    Time: O(n), Space: O(n)
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way: (1)
    dp[2] = 2  # 2 ways: (1+1), (2)

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main():
    n = 5
    print(climb_stairs_optimized(n))
    print(climb_stairs_dp(n))


if __name__ == "__main__":
    main()
