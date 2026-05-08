from collections import deque, defaultdict

class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        MAXV = max(nums)

        # Smallest Prime Factor sieve
        spf = list(range(MAXV + 1))
        for i in range(2, int(MAXV ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXV + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x >= 2 and spf[x] == x

        # Map: prime factor -> indices divisible by it
        divisible = defaultdict(list)

        for i, x in enumerate(nums):
            val = x
            factors = set()

            while val > 1:
                p = spf[val]
                factors.add(p)
                while val % p == 0:
                    val //= p

            for p in factors:
                divisible[p].append(i)

        # BFS
        q = deque([0])
        visited = [False] * n
        visited[0] = True

        used_prime = set()
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # Adjacent moves
                for ni in (i - 1, i + 1):
                    if 0 <= ni < n and not visited[ni]:
                        visited[ni] = True
                        q.append(ni)

                # Prime teleportation
                val = nums[i]
                if is_prime(val) and val not in used_prime:
                    used_prime.add(val)

                    for ni in divisible[val]:
                        if not visited[ni]:
                            visited[ni] = True
                            q.append(ni)

            steps += 1

        return -1
