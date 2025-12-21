class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        
        # sorted_pairs[i] == True means strs[i] < strs[i+1] already determined
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        
        for c in range(m):
            # Check if keeping column c would violate order for any unresolved pair
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break
            
            if bad:
                deletions += 1
                continue
            
            # Keep column c: update which pairs become resolved
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][c] < strs[i + 1][c]:
                    sorted_pairs[i] = True
        
        return deletions
