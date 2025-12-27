import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()  # sort by start time

        available = list(range(n))
        heapq.heapify(available)

        busy = []  # (end_time, room)
        count = [0] * n

        for s, e in meetings:
            # free rooms that have finished by time s
            while busy and busy[0][0] <= s:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            duration = e - s

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (e, room))
            else:
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        # find room with max meetings (tie -> smallest index)
        best = 0
        for i in range(1, n):
            if count[i] > count[best]:
                best = i
        return best
