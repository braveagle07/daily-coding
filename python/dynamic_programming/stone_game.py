"""LeetCode 877 - Stone Game.

Alice and Bob alternately take a pile from either end of `piles`; Alice
moves first. The total number of stones is odd and the number of piles is
even, so there are no ties. Return True if Alice wins with optimal play.
"""


class Solution(object):
    def stoneGame(self, piles):
        # Alice always wins. With an even number of piles she can choose to
        # take either all the even-indexed piles or all the odd-indexed ones,
        # and because the total is odd one of those sets is strictly larger.
        # Time: O(1), Space: O(1)
        return True

    def stoneGameDP(self, piles):
        """General interval DP that does not rely on the math trick.

        dp[i][j] = best score difference (current player - opponent) the
        player to move can force on the sub-array piles[i..j].
        Time: O(n^2), Space: O(n^2)
        """
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    piles[i] - dp[i + 1][j],
                    piles[j] - dp[i][j - 1],
                )

        return dp[0][n - 1] > 0
