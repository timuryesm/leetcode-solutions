class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        res = float('inf')
        
        for i, word in enumerate(words):
            if word == target:
                d = abs(i - startIndex)
                res = min(res, d, n - d)
        
        return res if res != float('inf') else -1
