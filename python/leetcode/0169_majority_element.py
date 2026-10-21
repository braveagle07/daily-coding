"""LeetCode 169 - Majority Element.

Return the element that appears more than n // 2 times. A majority element
is guaranteed to exist.

Boyer-Moore voting: keep a candidate and a counter. A different element
cancels one vote of the candidate; when the counter hits zero, the next
element becomes the new candidate. The majority element outnumbers all the
others combined, so it is the one left standing.
Time: O(n), Space: O(1)
"""


class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


if __name__ == "__main__":
    solution = Solution()
    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([7]) == 7
    assert solution.majorityElement([1, 2, 2]) == 2
    print("All Majority Element checks passed")
