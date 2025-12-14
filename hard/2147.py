class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        total_seats = corridor.count('S')
        if total_seats == 0 or total_seats % 2 == 1:
            return 0
        if total_seats == 2:
            return 1
        
        ways = 1
        seat_count = 0
        plants_between = 0
        counting_gap = False  # true after we complete a pair
        
        for ch in corridor:
            if ch == 'S':
                seat_count += 1
                
                if seat_count % 2 == 0:
                    # completed a pair; start counting plants until next seat
                    counting_gap = True
                    plants_between = 0
                else:
                    # this is the first seat of the next pair
                    if counting_gap:
                        # close the gap: multiply by (plants_between + 1)
                        ways = (ways * (plants_between + 1)) % MOD
                        counting_gap = False
            else:  # 'P'
                if counting_gap:
                    plants_between += 1
        
        return ways
