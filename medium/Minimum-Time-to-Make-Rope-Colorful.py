class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total = 0
        n = len(colors)
        i = 0

        # For each run of equal colors, remove all but the most "expensive" balloon
        # cost = sum(run) - max(run)
        while i < n:
            j = i
            run_sum = 0
            run_max = 0
            ch = colors[i]
            while j < n and colors[j] == ch:
                t = neededTime[j]
                run_sum += t
                if t > run_max:
                    run_max = t
                j += 1
            total += run_sum - run_max
            i = j

        return total
