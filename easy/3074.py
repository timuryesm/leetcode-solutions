class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total = sum(apple)
        capacity.sort(reverse=True)

        used = 0
        cur = 0
        for cap in capacity:
            cur += cap
            used += 1
            if cur >= total:
                return used

        return used  # guaranteed possible by constraints
