# LeetCode 344. Reverse String
# Idea: two pointers, swap the ends and move inward until they meet. Done in place.
# Time: O(n), Space: O(1)

class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
