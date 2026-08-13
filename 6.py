# Day 6 - LeetCode-style function practice in Python
# Problem: Two Sum
def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i

    return []
def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

if __name__ == "__main__":
    main()
