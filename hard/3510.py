import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        
        # Check if already non-decreasing
        is_sorted = True
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                break
        if is_sorted:
            return 0

        # Doubly linked list to manage deletions and neighbors efficiently
        # prev_idx and next_idx store the indices of neighbors
        prev_idx = [i - 1 for i in range(n)]
        next_idx = [i + 1 for i in range(n)]
        next_idx[n - 1] = -1
        
        # Min-priority queue to find the leftmost pair with minimum sum
        # Element format: (sum, left_index, right_index)
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (nums[i] + nums[i+1], i, i + 1))
            
        ops = 0
        current_nums = list(nums)
        active_indices = [True] * n
        
        while pq:
            s, l, r = heapq.heappop(pq)
            
            # Validity check: indices must be active and still adjacent
            if not active_indices[l] or not active_indices[r] or next_idx[l] != r:
                continue
            
            # Check if current state is non-decreasing
            # To avoid O(N) checks, we only stop when no "bad" pairs remain.
            # However, the problem asks for minimum ops to make it non-decreasing.
            # The greedy simulation follows the specific rule provided.
            
            # Perform operation: Merge r into l
            current_nums[l] = s
            active_indices[r] = False
            ops += 1
            
            # Update linked list
            new_r_neighbor = next_idx[r]
            next_idx[l] = new_r_neighbor
            if new_r_neighbor != -1:
                prev_idx[new_r_neighbor] = l
            
            # Check if the array is now non-decreasing
            # Optimization: only check near the modification or maintain a count of inversions
            # For the sake of this implementation, we re-verify sortedness 
            # as required by the simulation logic.
            temp_idx = 0
            while prev_idx[temp_idx] != -1: # find head
                temp_idx = prev_idx[temp_idx]
            
            sorted_check = True
            curr = temp_idx
            while next_idx[curr] != -1:
                if current_nums[curr] > current_nums[next_idx[curr]]:
                    sorted_check = False
                    break
                curr = next_idx[curr]
            
            if sorted_check:
                return ops
            
            # Add new potential pairs formed by the merge
            # Pair to the left: (prev_idx[l], l)
            if prev_idx[l] != -1:
                heapq.heappush(pq, (current_nums[prev_idx[l]] + current_nums[l], prev_idx[l], l))
            # Pair to the right: (l, next_idx[l])
            if next_idx[l] != -1:
                heapq.heappush(pq, (current_nums[l] + current_nums[next_idx[l]], l, next_idx[l]))
                
        return ops
