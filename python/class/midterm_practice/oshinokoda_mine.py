
example =  [[0, 1, 4, 4, 2],
            [1, 0, 4, 3, 3],
            [2, 2, 3, 0 ,2],
            [2, 4, 1, 2, 2],
            [1, 4, 0, 1, 3]]

stars = int(input())
matrix_size = int(input())

rows = []
for i in range(matrix_size):
    x = [int(x) for x in input().split()]
    rows.append(x)

result = []
for i in range(stars):
    y = input().split()
    result.append(y)



for i in range(stars):
    r = int(result[i][0])
    c = int(result[i][1])
    
    total_r = 0 #row section
    total_c = 0 #column sectionn
    total_cD = 0 #clockwise diagonal
    total_aD = 0 #anti-clockwise diagonal
    
    for i in range(matrix_size):
        total_r += int(rows[r][i])
        total_c += int(rows[i][c])

    for i in range(-matrix_size, matrix_size):
        if r + i < 0:
            continue
        elif r + i >= 0 and r + i < matrix_size:
            xcord = r + i
        elif r + i >= matrix_size:
            break
        
        if c + i < 0:
            continue
        elif c + i >= 0 and c + i < matrix_size:
            ycord = c + i
        elif c + i >= matrix_size:
            break
        
        try:
            total_cD += rows[xcord][ycord]
        except IndexError:
            continue
    
    for i in range(-matrix_size, matrix_size):
        if r + i < 0:
            continue
        elif r + i >= 0 and r + i < matrix_size:
            xcord = r + i
        elif r + i >= matrix_size:
            break
        
        if c - i < 0:
            continue
        elif c - i >= 0 and c - i < matrix_size:
            ycord = c - i
        elif c - i >= matrix_size:
            continue
        
        try:
            total_aD += rows[xcord][ycord]
        except IndexError:
            continue
        
        
    total = total_r + total_c + total_aD + total_cD - (int(rows[r][c]) * 3)
    print(total)


    