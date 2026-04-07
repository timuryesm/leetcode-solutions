class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
        
        self.cycle = 2 * (width + height) - 4

    def step(self, num):
        num %= self.cycle
        
        # Special case: full cycle → direction becomes South
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dir = 3
            return
        
        for _ in range(num):
            dx, dy = [(1,0), (0,1), (-1,0), (0,-1)][self.dir]
            nx, ny = self.x + dx, self.y + dy
            
            # If out of bounds → turn left
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir = (self.dir + 1) % 4
                dx, dy = [(1,0), (0,1), (-1,0), (0,-1)][self.dir]
                nx, ny = self.x + dx, self.y + dy
            
            self.x, self.y = nx, ny

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return ["East", "North", "West", "South"][self.dir]
