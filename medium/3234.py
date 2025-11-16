class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        m = len(zeros)

        if m == 0:
            return n * (n + 1) // 2

        # count all-ones substrings (z = 0 case)
        ans = 0
        run = 0
        for ch in s:
            if ch == '1':
                run += 1
            else:
                if run:
                    ans += run * (run + 1) // 2
                    run = 0
        if run:
            ans += run * (run + 1) // 2

        # sentinels for zero windows
        P = [-1] + zeros + [n]

        # max z such that z*(z+1) <= n
        import math
        Zmax = int((math.sqrt(1.0 + 4.0 * n) - 1.0) / 2.0)
        while Zmax * (Zmax + 1) > n:
            Zmax -= 1
        if Zmax > m:
            Zmax = m

        def count_pairs_ge(L, R, T):
            """Count pairs (a,b) with a∈[0..L-1], b∈[0..R-1], a+b >= T."""
            if T <= 0:
                return L * R
            if T > (L - 1) + (R - 1):
                return 0
            # Count pairs with a+b <= S then subtract from total
            S = T - 1
            if L > R:
                L, R = R, L  # ensure L <= R
            # Now L <= R
            if S < L:
                cnt_le = (S + 1) * (S + 2) // 2
            elif S < R:
                cnt_le = L * (S + 1) - (L - 1) * L // 2
            else:
                t = S - (R - 1)  # 0 <= t <= L-1
                cnt_le = (t + 1) * R
                cnt_le += (L - t - 1) * (S + 1) - ((L + t) * (L - t - 1) // 2)
            return L * R - cnt_le

        # z >= 1 windows
        for z in range(1, Zmax + 1):
            Lmin = z * (z + 1)
            # slide over windows of z zeros
            for j in range(0, m - z + 1):
                left_choices = P[j + 1] - P[j]
                right_choices = P[j + z + 1] - P[j + z]
                core_len = P[j + z] - P[j + 1] + 1  # span from first to last zero inclusive
                need = Lmin - core_len  # need a+b >= need
                if need <= 0:
                    ans += left_choices * right_choices
                elif need <= (left_choices - 1) + (right_choices - 1):
                    ans += count_pairs_ge(left_choices, right_choices, need)
                # else: impossible for this window, skip

        return ans
