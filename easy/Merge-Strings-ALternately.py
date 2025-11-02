class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        i = j = 0
        n1, n2 = len(word1), len(word2)

        while i < n1 or j < n2:
            if i < n1:
                res.append(word1[i])
                i += 1
            if j < n2:
                res.append(word2[j])
                j += 1

        return "".join(res)
