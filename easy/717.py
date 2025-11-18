class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)

        while i < n - 1:    # stop before last because we want to check if last is single
            if bits[i] == 1:
                i += 2      # two-bit char
            else:
                i += 1      # one-bit char

        return i == n - 1
