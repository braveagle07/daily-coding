# Day 2 - July 9, 2026
# 3 Simple Python Problems

# Problem 1: Reverse a string
def reverse_string(s):
    return s[::-1]

# Problem 2: Find the largest number in a list
def find_largest(numbers):
    return max(numbers)

# Problem 3: Count vowels in a string
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')

if __name__ == '__main__':
    print(reverse_string('hello'))          
    print(find_largest([3, 7, 1, 9, 4]))    # 9
    print(count_vowels('Vasanth sesetti'))  # 6
