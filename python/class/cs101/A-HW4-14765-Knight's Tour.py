r, c = map(int, input().split())


stepCount = 0
matrix = [[-1 for _ in range(c)] for _ in range(r)]

moves = [(2, 1),
         (2, -1),
         (-2, 1),
         (-2, -1),
         (1, 2),
         (1, -2), 
         (-1, 2), 
         (-1, -2)] 

matrix[0][0] = 0

posR = 0
posC = 0

def move(posR, posC, stepCount):
    if stepCount == r * c - 1:
        return True
        
    for dr, dc in moves:
        
        
        nextR = posR + dr
        nextC = posC + dc
        
        if 0 <= nextR < r and 0 <= nextC < c and matrix[nextR][nextC] == -1:
            matrix[nextR][nextC] = stepCount + 1

            if move(nextR, nextC, stepCount + 1):
                return True
            
            matrix[nextR][nextC] = -1
        
    return False
            
            
if move(posR, posC, stepCount):
    print(matrix)