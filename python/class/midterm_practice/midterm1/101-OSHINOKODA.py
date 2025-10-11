stars = int(input())
matrix_size = int(input())


row_sum = [0] * matrix_size
col_sum = [0] * matrix_size
cD = {}  
aD = {}
rows_values = [] 

for r in range(matrix_size):
    row = list(map(int, input().split()))
    for c in range(matrix_size):
        value = row[c]
        row_sum[r] += value
        col_sum[c] += value
        cD[r - c] = cD.get(r - c, 0) + value
        aD[r + c] = aD.get(r + c, 0) + value
    rows_values.append(row) 
results = []

for _ in range(stars):
    r, c = map(int, input().split())
    value = rows_values[r][c]
    total_rows = row_sum[r]
    total_cols = col_sum[c]
    total_cDiag = cD[r - c]
    total_aDiag = aD[r + c]


    total = total_rows + total_cols + total_cDiag + total_aDiag - 3 * value
    print(total)
