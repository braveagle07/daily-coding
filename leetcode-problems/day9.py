class Solution(object):
    def isConsecutive(self, nums):
        n = len(nums)
        mn = min(nums)
        mx = max(nums)

        return mx - mn + 1 == n and len(set(nums)) == n