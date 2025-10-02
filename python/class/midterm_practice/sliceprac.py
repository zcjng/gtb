x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
    ]



rows = len(x)
cols = len(x[0])

result = []

currentRow = currentCol = 0
goingUp = True

while len(result) != rows * cols:
    if goingUp:
        while currentRow >= 0 and currentCol < cols:
            result.append(str(x[currentRow][currentCol]))
            
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
            result.append(str(x[currentRow][currentCol]))
            
            currentCol -= 1
            currentRow += 1
        
        if currentRow == rows:
            currentCol += 2
            currentRow -= 1
        else:
            currentCol += 1
            
        goingUp = True
        
print("".join(result))
        
    
    