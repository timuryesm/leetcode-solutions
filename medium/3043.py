class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        
        # Step 1: Accumulate all possible prefixes from numbers in arr1
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10  # Remove the last digit to get the next prefix
        
        max_length = 0
        
        # Step 2: Check prefixes of numbers in arr2 against the stored prefixes
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    # Found a common prefix; measure its digit length
                    max_length = max(max_length, len(str(val)))
                    # Since we check from longest to shortest prefix for this number,
                    # we can break early once the longest match is found
                    break
                val //= 10  # Drop the last digit to check the next shorter prefix
                
        return max_length
