class Solution(object):
    def mostWordsFound(self, sentences):
        return max(len(word.split()) for word in sentences)
