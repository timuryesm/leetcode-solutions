class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        events = {}
        total = 0

        for x, y, l in squares:
            total += l * l
            events[y] = events.get(y, 0) + l
            events[y + l] = events.get(y + l, 0) - l

        half = total / 2.0

        ys = sorted(events.keys())
        cur_area = 0.0
        cur_slope = 0.0
        prev_y = ys[0]

        # Before first event: slope is 0, area is 0. Then apply first event at prev_y.
        cur_slope += events[prev_y]

        # If half is 0 (not really possible with positive squares), minimal y is prev_y
        if half == 0.0:
            return float(prev_y)

        for i in range(1, len(ys)):
            y = ys[i]

            # If we already hit half exactly at the start of this segment, minimal y is prev_y
            if cur_area == half:
                return float(prev_y)

            dist = y - prev_y
            if dist > 0:
                next_area = cur_area + cur_slope * dist

                # If half lies within [cur_area, next_area], solve linearly
                if cur_slope != 0.0 and cur_area <= half <= next_area:
                    return prev_y + (half - cur_area) / cur_slope

                cur_area = next_area

            # Apply slope changes at y
            cur_slope += events[y]
            prev_y = y

        # After processing all events, cur_area should be total.
        # If half equals total (not possible unless total==0), return last y.
        return float(prev_y)
