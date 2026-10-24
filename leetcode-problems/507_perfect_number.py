# LeetCode 507. Perfect Number
# A perfect number equals the sum of its proper divisors (all divisors except itself).
# This is the simple O(n) version; for large n loop only up to sqrt(n) (O(sqrt n)).

class Solution:
    def isPerfect(self, n: int) -> bool:
        total = 0

        for i in range(1, n):
            if n % i == 0:
                total += i

        return total == n
