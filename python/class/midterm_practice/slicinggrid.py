def solve(n, d, grid):
    
    rows = len(grid)
    cols = len(grid[0])

    result = []

    currentRow = currentCol = 0
    
    if d == 1:
        goingUp = True
    else:
        goingUp = False
    

    while len(result) != rows * cols:
        if goingUp:
            while currentRow >= 0 and currentCol < cols:
                result.append(str(grid[currentRow][currentCol]))
                
                currentRow -= 1
                currentCol += 1
                
            if currentCol == cols:
                currentRow += 2
                currentCol -= 1
            else:
                currentRow += 1
                
            goingUp = False
        else:
            while currentCol >= 0 and currentRow < rows:
                result.append(str(grid[currentRow][currentCol]))
                
                currentCol -= 1
                currentRow += 1
            
            if currentRow == rows:
                currentCol += 2
                currentRow -= 1
            else:
                currentCol += 1
                
            goingUp = True
            
    return "".join(result)

_n, _d = map(int, input().split())

_grid = []
for _ in range(_n):
    _row = []
    for num in input().split():
        _row.append(int(num))
    _grid.append(_row)
    
    
print(solve(_n, _d, _grid))