import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        # Doubly Linked List to handle O(1) removals
        val = [x for x in nums]
        nxt = list(range(1, n + 1))
        prv = list(range(-1, n - 1))
        
        # Priority Queue for greedy selection: (sum, leftmost_index)
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (val[i] + val[i+1], i))
        
        # Helper to check if a pair at index i is "bad" (unsorted)
        def is_bad(i):
            if i < 0 or i >= n: return False
            j = nxt[i]
            return j < n and val[i] > val[j]

        # Initial bad_count
        bad_count = 0
        for i in range(n - 1):
            if is_bad(i):
                bad_count += 1
        
        if bad_count == 0:
            return 0

        ans = 0
        removed = [False] * n
        
        while bad_count > 0 and pq:
            s, i = heapq.heappop(pq)
            
            # Lazy removal check
            j = nxt[i]
            if removed[i] or j >= n or (val[i] + val[j] != s):
                continue
            
            # 1. Remove old "bad" statuses before updating values
            if is_bad(prv[i]): bad_count -= 1
            if is_bad(i):      bad_count -= 1
            if is_bad(j):      bad_count -= 1
            
            # 2. Perform the Merge
            val[i] = s
            removed[j] = True
            
            # 3. Update Doubly Linked List pointers
            new_nxt = nxt[j]
            nxt[i] = new_nxt
            if new_nxt < n:
                prv[new_nxt] = i
            
            # 4. Re-check "bad" statuses for the modified elements
            if is_bad(prv[i]): bad_count += 1
            if is_bad(i):      bad_count += 1
            
            ans += 1
            if bad_count <= 0:
                return ans
            
            # 5. Push new potential pairs to the heap
            if prv[i] != -1:
                heapq.heappush(pq, (val[prv[i]] + val[i], prv[i]))
            if nxt[i] < n:
                heapq.heappush(pq, (val[i] + val[nxt[i]], i))
                
        return ans
