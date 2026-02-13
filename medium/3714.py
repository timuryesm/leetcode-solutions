class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0

        # 1) One distinct character: longest same-char run
        run = 1
        ans = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run += 1
            else:
                run = 1
            if run > ans:
                ans = run

        # Helper: best balanced substring using exactly two letters
        # by forbidding the third letter. Works in O(n).
        def best_two_letters(forbidden):
            # remaining two letters
            letters = []
            for ch in ('a', 'b', 'c'):
                if ch != forbidden:
                    letters.append(ch)
            inc_ch, dec_ch = letters[0], letters[1]

            best = 0
            diff = 0
            first = {0: -1}  # will be reset at segment boundaries

            for i, ch in enumerate(s):
                if ch == forbidden:
                    # reset segment; "position before segment start" is i
                    diff = 0
                    first = {0: i}
                    continue

                if ch == inc_ch:
                    diff += 1
                else:  # ch == dec_ch
                    diff -= 1

                if diff in first:
                    length = i - first[diff]
                    if length > best:
                        best = length
                else:
                    first[diff] = i

            return best

        # 2) Two distinct chars: forbid each letter once
        ans = max(ans, best_two_letters('a'))
        ans = max(ans, best_two_letters('b'))
        ans = max(ans, best_two_letters('c'))

        # 3) Three distinct chars: equal counts of a, b, c
        a = b = c = 0
        seen = {(0, 0): -1}
        best3 = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            key = (a - b, a - c)
            if key in seen:
                length = i - seen[key]
                if length > best3:
                    best3 = length
            else:
                seen[key] = i

        ans = max(ans, best3)
        return ans
