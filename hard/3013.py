import heapq

class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        need = k - 2

        self.small = []   # max-heap (store -value)
        self.large = []   # min-heap
        self.del_s = {}
        self.del_l = {}
        self.in_small = [False] * n

        self.small_size = 0
        self.large_size = 0
        self.small_sum = 0

        def prune(heap, delayed, is_small):
            while heap:
                val, idx = heap[0]
                if idx in delayed:
                    heapq.heappop(heap)
                    delayed[idx] -= 1
                    if delayed[idx] == 0:
                        del delayed[idx]
                else:
                    break

        def rebalance():
            prune(self.small, self.del_s, True)
            prune(self.large, self.del_l, False)

            while self.small_size > need:
                v, i = heapq.heappop(self.small)
                v = -v
                self.in_small[i] = False
                self.small_sum -= v
                self.small_size -= 1
                heapq.heappush(self.large, (v, i))
                self.large_size += 1

            while self.small_size < need and self.large:
                v, i = heapq.heappop(self.large)
                self.in_small[i] = True
                self.small_sum += v
                self.small_size += 1
                self.large_size -= 1
                heapq.heappush(self.small, (-v, i))

        def add(i):
            v = nums[i]
            if self.small_size < need:
                heapq.heappush(self.small, (-v, i))
                self.in_small[i] = True
                self.small_sum += v
                self.small_size += 1
            else:
                prune(self.small, self.del_s, True)
                if need > 0 and self.small and v < -self.small[0][0]:
                    tv, ti = heapq.heappop(self.small)
                    tv = -tv
                    self.small_sum -= tv
                    self.in_small[ti] = False
                    heapq.heappush(self.large, (tv, ti))
                    self.large_size += 1

                    heapq.heappush(self.small, (-v, i))
                    self.in_small[i] = True
                    self.small_sum += v
                else:
                    heapq.heappush(self.large, (v, i))
                    self.large_size += 1
            rebalance()

        def remove(i):
            v = nums[i]
            if self.in_small[i]:
                self.del_s[i] = self.del_s.get(i, 0) + 1
                self.small_sum -= v
                self.small_size -= 1
            else:
                self.del_l[i] = self.del_l.get(i, 0) + 1
                self.large_size -= 1
            rebalance()

        # initialize window
        for i in range(2, min(n, 2 + dist)):
            add(i)

        res = float('inf')
        last = n - (k - 1)

        for i1 in range(1, last + 1):
            res = min(res, nums[0] + nums[i1] + self.small_sum)

            out_i = i1 + 1
            in_i = i1 + dist + 1

            if out_i < n:
                remove(out_i)
            if in_i < n:
                add(in_i)

        return res
