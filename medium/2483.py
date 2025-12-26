class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        penalty = customers.count('Y')  # closing at hour 0
        best_penalty = penalty
        best_hour = 0
        
        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1
            else:  # 'N'
                penalty += 1
            
            # closing at hour i+1
            if penalty < best_penalty:
                best_penalty = penalty
                best_hour = i + 1
        
        return best_hour
