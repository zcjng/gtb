import sys
input = sys.stdin.readline

T = int(input())
N = int(input())

row_sum = [0] * N
col_sum = [0] * N
diag_main = [0] * (2 * N - 1)   
diag_anti = [0] * (2 * N - 1)  

matrix = []
for r in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    for c in range(N):
        val = row[c]
        row_sum[r] += val
        col_sum[c] += val
        diag_main[r - c + N - 1] += val
        diag_anti[r + c] += val

queries = [tuple(map(int, input().split())) for _ in range(T)]

results = []
for r, c in queries:
    val = matrix[r][c]
    total = row_sum[r] + col_sum[c] + diag_main[r - c + N - 1] + diag_anti[r + c] - 3 * val
    results.append(total)

print('\n'.join(map(str, results)))
