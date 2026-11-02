class Solution:
    def capitalize_first_last(self, s: str) -> str:
        words = s.split()
        ans = []

        for word in words:
            if len(word) == 1:
                ans.append(word.upper())
            else:
                ans.append(word[0].upper() + word[1:-1] + word[-1].upper())

        return " ".join(ans)
