# Day 6 - LeetCode-style function practice in Python
# Problem: Two Sum
def two_sum(nums, target):
    """Return the indices of the two numbers that add up to target.

    One pass with a hash map: for each number, check whether its complement
    (target - number) was already seen, otherwise remember the current index.
    Time: O(n), Space: O(n)
    Returns [] if no pair exists (LeetCode guarantees one, so this is just a
    safe default).
    """
    seen = {}

    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i

    return []


def main():
    # Basic case, duplicate values, negatives, and no-solution input.
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert two_sum([1, 2, 3], 100) == []
    print(two_sum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    main()
