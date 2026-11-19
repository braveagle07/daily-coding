class Solution:
    def sortIt(self, arr):
        odd = []
        even = []

        for x in arr:
            if x % 2 != 0:
                odd.append(x)
            else:
                even.append(x)

        odd.sort(reverse=True)  # Descending
        even.sort()             # Ascending

        arr[:] = odd + even
