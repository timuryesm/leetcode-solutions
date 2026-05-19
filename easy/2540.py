class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Initialize two pointers at the beginning of each array
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        
        # Traverse through both arrays
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                return nums1[i]  # Found the smallest common element!
            elif nums1[i] < nums2[j]:
                i += 1  # Move the pointer in nums1 forward
            else:
                j += 1  # Move the pointer in nums2 forward
                
        # If the loop finishes without finding any common element
        return -1
