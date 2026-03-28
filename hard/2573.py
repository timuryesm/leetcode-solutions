class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)
        
        # Step 1: basic validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        # Step 2: build string
        res = [''] * n
        curr_char = 0
        
        for i in range(n):
            if res[i] == '':
                if curr_char >= 26:
                    return ""
                c = chr(ord('a') + curr_char)
                curr_char += 1
                
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = c
        
        word = "".join(res)
        
        # Step 3: validate by recomputing LCP
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0
                
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word
