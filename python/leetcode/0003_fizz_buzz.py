"""LeetCode 412 - Fizz Buzz.

Return a list of strings for 1..n: "FizzBuzz" for multiples of 15, "Fizz"
for multiples of 3, "Buzz" for multiples of 5, otherwise the number itself.
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # Check 15 first, otherwise multiples of 3 or 5 would shadow it.
        # Time: O(n), Space: O(n) for the output list.
        answer = []

        for number in range(1, n + 1):
            if number % 15 == 0:
                answer.append("FizzBuzz")
            elif number % 3 == 0:
                answer.append("Fizz")
            elif number % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(number))

        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.fizzBuzz(1) == ["1"]
    assert solution.fizzBuzz(3) == ["1", "2", "Fizz"]
    assert solution.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert solution.fizzBuzz(15)[-1] == "FizzBuzz"
    print("All Fizz Buzz checks passed")
