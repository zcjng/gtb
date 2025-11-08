class Potato:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.score = 0

    def play(self, time:int, maze:"Maze"):
        # Update maze (if there's any event, do the event first)
        maze.update_time(time, self)
        
        self.score += maze.pick_up_treasure_at(self.i,self.j)
        
        moves = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        
        for di, dj in moves:
            ni = self.i + di
            nj = self.j + dj
            if maze.is_cell_walkable(ni, nj):
                self.i, self.j = ni, nj
                break
        
        # TODO
        # utilize functions in maze
        # 1. pick up the points where you're standing on (take a look in 'class Maze')
        # 2. move Potato by checking if next cell is a stone by the priority of [Right, Down, Left, Up]

    def get_location_message(self, time:int):
        # TODO
        # return the formated the message by the required format 
        # >> the message printed each second
        return f"Potato arrives at ({self.i}, {self.j}) when t={time}"

    def get_summary_message(self, time:int):
        # TODO
        # return the formated the message by the required format 
        # >> the message printed when Potato arrived at bottom right
        return f"Potato spent {time} seconds and got {self.score} points"


class MazeRotatingEvent:
    def __init__(self, t, i, j, w, d):
        self.t = t
        self.i = i
        self.j = j
        self.w = w
        self.d = d


class Maze:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def read_grid(self):
        self.grid = [list(map(int, input().split())) for i in range(self.n)]

    def read_k_events(self, k:int):
        self.events = {} # TODO replace this with how you want to store MazeRotatingEvents
        for i in range(k):
            t, i, j, w, d = map(int, input().split())
            rotatingEvent = MazeRotatingEvent(t, i, j, w, d)
            self.events[t] = rotatingEvent
            # TODO store this new MazeRotatingEvent <rotatingEvent>

    def is_cell_the_end(self, i:int, j:int):
        return i == self.n - 1 and j == self.m - 1

    def is_cell_walkable(self, i:int, j:int):
        # TODO
        # return False if (i, j) is out of map or is a stone (negative number)
        # return True if (i, j) is in the map and is not a stone (positive number or 0)
        return 0 <= i < self.n and 0 <=  j < self.m and self.grid[i][j] >= 0

    def pick_up_treasure_at(self, i:int, j:int):
        # TODO
        # return the points on (i, j), and because it's picked up, subtract by 1
        val = self.grid[i][j]
        self.grid[i][j] -= 1
        return val

    def update_time(self, time:int, potato:Potato):
        # TODO
        # check if there's a rotating event on time <time>
        # if there's a rotating event, rotate the area, and also move potato's position
        if self.events.get(time):
            event = self.events[time]
            
            dest = [rows[:] for rows in self.grid]
            
            d = event.d
            width = event.w
            i = event.i - width // 2
            j = event.j - width // 2
            rotated = False
            
            oldi = potato.i
            oldj = potato.j
            if d == 0:
                for x in range(width):
                    for y in range(width):
                        dest[y + i][width - x - 1 + j] = self.grid[x + i][y + j]
                        if oldi == x + i and oldj == y + j and rotated == False:
                            potato.i = y + i
                            potato.j = width - x - 1 + j
                            rotated = True

                self.grid = dest
            else:
                for x in range(width):
                    for y in range(width):
                        dest[width - y - 1 + i][x + j] = self.grid[x + i][y + j]
                        if oldi == x + i and oldj == y + j and rotated == False:
                            potato.i = width - y - 1 + i
                            potato.j = x + j
                            rotated = True
                self.grid = dest
                

n, m, k = map(int, input().split())

magic_maze = Maze(n, m)
magic_maze.read_grid()
magic_maze.read_k_events(k)

cute_potato = Potato()

time = 0
while(True):
    old_i, old_j = cute_potato.i, cute_potato.j
    cute_potato.play(time, magic_maze)

    print(cute_potato.get_location_message(time))

    if(magic_maze.is_cell_the_end(cute_potato.i, cute_potato.j)):
        print(cute_potato.get_summary_message(time))
        break

    time += 1
