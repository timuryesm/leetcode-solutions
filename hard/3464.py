class Solution(object):
    def maxDistance(self, side, points, k):
        def pos(x, y):
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 3 * side - x
            return 4 * side - y

        arr = sorted(pos(x, y) for x, y in points)
        n = len(arr)
        P = 4 * side
        arr += [x + P for x in arr]

        def can(d):
            m = len(arr)
            nxt = [m] * m

            j = 0
            for i in range(m):
                if j < i + 1:
                    j = i + 1
                while j < m and arr[j] - arr[i] < d:
                    j += 1
                nxt[i] = j

            for start in range(n):
                cur = start
                ok = True

                for _ in range(k - 1):
                    cur = nxt[cur]
                    if cur >= start + n:
                        ok = False
                        break

                if ok and arr[cur] - arr[start] <= P - d:
                    return True

            return False

        left, right = 1, side

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
