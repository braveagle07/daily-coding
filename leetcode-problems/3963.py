class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        return ["." * n] + [".".rjust(n, "#")] * (m - 1)
        