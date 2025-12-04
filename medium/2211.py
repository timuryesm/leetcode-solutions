class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        n = len(directions)
        i, j = 0, n - 1

        # Skip all left-moving cars at the far left (they never collide)
        while i < n and directions[i] == 'L':
            i += 1

        # Skip all right-moving cars at the far right (they never collide)
        while j >= 0 and directions[j] == 'R':
            j -= 1

        # Now all potential collisions happen in directions[i:j+1]
        # Every non-'S' in this interval will collide exactly once.
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1

        return collisions
