# Day 1 - July 8, 2026
# Problem: Find the sum of all even numbers in a list
# Platform: Daily Practice

def sum_of_evens(numbers):
    """Return the sum of all even numbers in a list."""
    return sum(num for num in numbers if num % 2 == 0)

def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(' ', '')
    return s == s[::-1]

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'Sum of evens in {nums}: {sum_of_evens(nums)}')

    words = ['racecar', 'hello', 'madam', 'python']
    for word in words:
        print(f'{word} is palindrome: {is_palindrome(word)}')
