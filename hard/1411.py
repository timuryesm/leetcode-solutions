class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7

        # For one row:
        # "ABA" patterns: 3 choices for A, 2 for B => 6
        # "ABC" patterns: 3 choices for A, 2 for B, 1 for C => 6
        aba = 6
        abc = 6

        for _ in range(2, n + 1):
            new_aba = (3 * aba + 2 * abc) % MOD
            new_abc = (2 * aba + 2 * abc) % MOD
            aba, abc = new_aba, new_abc

        return (aba + abc) % MOD
