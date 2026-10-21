"""LeetCode 2114 - Maximum Number of Words Found in Sentences.

Each sentence is a string of words separated by single spaces. Return the
largest word count among all sentences.

Time: O(total characters), Space: O(longest sentence) for the split list.
"""


class Solution(object):
    def mostWordsFound(self, sentences):
        return max(len(sentence.split()) for sentence in sentences)


if __name__ == "__main__":
    solution = Solution()
    assert solution.mostWordsFound(
        ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    ) == 6
    assert solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3
    assert solution.mostWordsFound(["hello"]) == 1
    print("All Most Words Found checks passed")
