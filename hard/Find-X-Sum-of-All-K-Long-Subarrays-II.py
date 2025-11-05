import heapq

class Solution(object):
    def findXSum(self, nums, k, x):
        n = len(nums)
        if k == 0 or n == 0:
            return []

        freq = {}          # value -> count in window
        in_top = {}        # value -> bool (is currently in top-x set)
        top = []           # min-heap of (freq, value, value)
        rest = []          # max-heap of (-freq, -value, value)
        sum_top = [0]      # wrap in list so inner funcs can mutate in Py2
        size_top = [0]

        def clean_top():
            while top:
                f, val, v = top[0]
                cur = freq.get(v, 0)
                if cur != f or not in_top.get(v, False):
                    heapq.heappop(top)
                else:
                    break

        def clean_rest():
            while rest:
                nf, nv, v = rest[0]
                f, val = -nf, -nv
                cur = freq.get(v, 0)
                if cur != f or in_top.get(v, False):
                    heapq.heappop(rest)
                else:
                    break

        def promote():
            clean_rest()
            if not rest:
                return False
            nf, nv, v = heapq.heappop(rest)
            f, val = -nf, -nv
            if freq.get(v, 0) != f or in_top.get(v, False):
                return False  # stale
            in_top[v] = True
            heapq.heappush(top, (f, val, v))
            size_top[0] += 1
            sum_top[0] += v * f
            return True

        def demote():
            clean_top()
            if not top:
                return False
            f, val, v = heapq.heappop(top)
            if freq.get(v, 0) != f or not in_top.get(v, False):
                return False  # stale
            in_top[v] = False
            heapq.heappush(rest, (-f, -val, v))
            size_top[0] -= 1
            sum_top[0] -= v * f
            return True

        def rebalance():
            distinct = len(freq)

            # shrink/grow to exactly min(x, distinct)
            while size_top[0] > min(x, distinct):
                if not demote():
                    clean_top()
                    if not top:
                        break
            while size_top[0] < min(x, distinct):
                if not promote():
                    clean_rest()
                    if not rest:
                        break

            # fix ordering between borders
            while True:
                clean_top()
                clean_rest()
                if not top or not rest:
                    break
                f_top, val_top, v_top = top[0]
                nf_rest, nv_rest, v_rest = rest[0]
                f_rest, val_rest = -nf_rest, -nv_rest
                # rest's best strictly better than top's worst?
                if (f_rest > f_top) or (f_rest == f_top and val_rest > val_top):
                    if not demote():
                        break
                    if not promote():
                        break
                else:
                    break

        # initialize first window
        for i in range(k):
            v = nums[i]
            freq[v] = freq.get(v, 0) + 1

        for v, f in freq.items():
            in_top[v] = False
            heapq.heappush(rest, (-f, -v, v))

        rebalance()
        ans = [sum_top[0]]

        # slide window
        for i in range(k, n):
            add_v = nums[i]
            rem_v = nums[i - k]

            # remove rem_v
            if rem_v in freq:
                old = freq[rem_v]
                new = old - 1
                if in_top.get(rem_v, False):
                    sum_top[0] += rem_v * (new - old)  # adjust by delta count
                    heapq.heappush(top, (new, rem_v, rem_v))
                else:
                    heapq.heappush(rest, (-new, -rem_v, rem_v))
                if new == 0:
                    del freq[rem_v]
                    if in_top.get(rem_v, False):
                        in_top[rem_v] = False
                        size_top[0] -= 1
                    else:
                        in_top.pop(rem_v, None)
                else:
                    freq[rem_v] = new

            # add add_v
            old = freq.get(add_v, 0)
            new = old + 1
            freq[add_v] = new
            if add_v not in in_top:
                in_top[add_v] = False
            if in_top.get(add_v, False):
                sum_top[0] += add_v * (new - old)
                heapq.heappush(top, (new, add_v, add_v))
            else:
                heapq.heappush(rest, (-new, -add_v, add_v))

            rebalance()
            ans.append(sum_top[0])

        return ans
