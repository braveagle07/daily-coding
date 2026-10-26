# LeetCode 1991. Find the Middle Index in Array
# Idea: keep a running left sum; right sum = total - left_sum - nums[i].
# The first index where left == right is the leftmost middle index.
# Time: O(n), Space: O(1)

class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
