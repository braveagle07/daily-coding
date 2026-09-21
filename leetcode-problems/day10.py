class Solution:
    def findMaximumPairs(self, students: str) -> int:
        c = 0
        i = 0

        while i < len(students) - 1:
            if students[i] != students[i + 1]:
                c += 1
                i += 2
            else:
                i += 1

        return c
