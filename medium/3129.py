class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        
        # dp0[z][o] = ways ending with 0
        # dp1[z][o] = ways ending with 1
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        # start with blocks
        for k in range(1, min(limit, zero)+1):
            dp0[k][0] = 1
            
        for k in range(1, min(limit, one)+1):
            dp1[0][k] = 1
        
        for z in range(zero+1):
            for o in range(one+1):
                
                # extend with zeros
                if dp1[z][o]:
                    for k in range(1, min(limit, zero-z)+1):
                        dp0[z+k][o] = (dp0[z+k][o] + dp1[z][o]) % MOD
                
                # extend with ones
                if dp0[z][o]:
                    for k in range(1, min(limit, one-o)+1):
                        dp1[z][o+k] = (dp1[z][o+k] + dp0[z][o]) % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD
