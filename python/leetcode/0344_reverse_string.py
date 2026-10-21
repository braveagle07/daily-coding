"""LeetCode 344 - Reverse String.

Reverse the list of characters `s` in place (return nothing, O(1) extra
memory).
"""


class Solution(object):
    def reverseString(self, s):
        """Two pointers: swap the ends and move inward.

        Time: O(n), Space: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseStringBuiltin(self, s):
        """Same result using the built-in list.reverse() (also in place)."""
        s.reverse()


if __name__ == "__main__":
    solution = Solution()
    for method in (solution.reverseString, solution.reverseStringBuiltin):
        chars = list("hello")
        method(chars)
        assert chars == list("olleh")

        chars = list("Hannah")
        method(chars)
        assert chars == list("hannaH")

        chars = []
        method(chars)
        assert chars == []

        chars = ["a"]
        method(chars)
        assert chars == ["a"]
    print("All Reverse String checks passed")
