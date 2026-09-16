#1st approach
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()
#2nd approach
class Solution(object):
    def toLowerCase(self, s):
        ans = ""

        for ch in s:
            if 'A' <= ch <= 'Z':
                ans += chr(ord(ch) + 32)
            else:
                ans += ch

        return ans
