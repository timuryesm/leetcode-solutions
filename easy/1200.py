class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        best = float('inf')
        res = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < best:
                best = diff
                res = [[arr[i - 1], arr[i]]]
            elif diff == best:
                res.append([arr[i - 1], arr[i]])
        return res
