class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        C = [0] * n
        
        # Array to track elements seen so far. 
        # Size n + 1 since numbers are 1-indexed (from 1 to n)
        seen_count = [0] * (n + 1)
        
        current_common = 0
        
        for i in range(n):
            # Process element from array A
            seen_count[A[i]] += 1
            if seen_count[A[i]] == 2:
                current_common += 1
                
            # Process element from array B
            seen_count[B[i]] += 1
            if seen_count[B[i]] == 2:
                current_common += 1
            
            # Store the current common count for prefix i
            C[i] = current_common
            
        return C
