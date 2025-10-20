
grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]

r = len(grid)
c = len(grid[0])


posR = 0
posC = 0

moves = [(2, 1),
         (2, -1),
         (-2, 1),
         (-2, -1),
         (1, 2),
         (1, -2), 
         (-1, 2), 
         (-1, -2)]

counter = 0

results = []
def move(posR, posC, counter):
    if counter == r * c - 1:
        return True
    
    for dr, dc in moves:
        nextR = posR + dr
        nextC = posC + dc
        
        if 0 <= nextR < r and 0 <= nextC < c and grid[nextR][nextC] == counter + 1:
            if move(nextR, nextC, counter + 1):
                return True
            
    return False

if move(posR, posC, counter):
    print('True')
else:
    print('False')