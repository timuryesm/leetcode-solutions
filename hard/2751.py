class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        # Step 1: Combine and sort by position
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(n)]
        )
        
        stack = []  # stack of indices in robots array
        alive = [True] * n
        
        for i in range(n):
            pos, health, direction, idx = robots[i]
            
            if direction == 'R':
                stack.append(i)
            else:
                # direction == 'L'
                while stack and robots[i][1] > 0:
                    j = stack[-1]
                    
                    if not alive[j]:
                        stack.pop()
                        continue
                    
                    # collision
                    if robots[j][1] < robots[i][1]:
                        # R robot dies
                        alive[j] = False
                        stack.pop()
                        robots[i] = (pos, robots[i][1] - 1, direction, idx)
                    
                    elif robots[j][1] > robots[i][1]:
                        # L robot dies
                        alive[i] = False
                        robots[j] = (
                            robots[j][0],
                            robots[j][1] - 1,
                            robots[j][2],
                            robots[j][3]
                        )
                        break
                    
                    else:
                        # equal → both die
                        alive[j] = False
                        alive[i] = False
                        stack.pop()
                        break
        
        # Collect survivors in original order
        result = []
        for i in range(n):
            if alive[i]:
                result.append((robots[i][3], robots[i][1]))
        
        # sort by original index
        result.sort()
        
        return [h for _, h in result]
