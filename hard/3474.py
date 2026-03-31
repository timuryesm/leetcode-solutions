class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        L = n + m - 1
        
        word = [''] * L
        forced = [False] * L
        
        # 1) Apply all T constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    ch = str2[j]
                    if forced[pos] and word[pos] != ch:
                        return ""
                    word[pos] = ch
                    forced[pos] = True
        
        # 2) Fill remaining positions with 'a'
        for i in range(L):
            if not forced[i]:
                word[i] = 'a'
        
        free_positions = [i for i in range(L) if not forced[i]]
        
        # Helper: binary search for rightmost free position in [l, r]
        def rightmost_free(l, r):
            lo, hi = 0, len(free_positions) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if free_positions[mid] <= r:
                    ans = free_positions[mid]
                    lo = mid + 1
                else:
                    hi = mid - 1
            if ans >= l:
                return ans
            return -1
        
        unsatisfied = []
        
        # 3) Find F windows that are still equal to str2
        for i in range(n):
            if str1[i] == 'F':
                equal = True
                has_free = False
                
                for j in range(m):
                    pos = i + j
                    if forced[pos]:
                        if word[pos] != str2[j]:
                            equal = False
                            break
                    else:
                        has_free = True
                        if str2[j] != 'a':
                            equal = False
                            break
                
                if equal:
                    if not has_free:
                        return ""
                    unsatisfied.append((i, i + m - 1))
        
        # 4) Greedily break unsatisfied F windows using rightmost free position
        last_changed = -1
        for l, r in unsatisfied:
            if last_changed >= l:
                continue
            
            pos = rightmost_free(l, r)
            if pos == -1:
                return ""
            
            word[pos] = 'b'
            last_changed = pos
        
        return "".join(word)
