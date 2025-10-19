m, n = map(int, input().split())

board = [["."] * n for i in range(n)]

col = set()
posDiag = set() #this is (r+c)
negDiag = set() #this is (r-c)

result = 0
def solve(rows, queens):
    global result
    
    if queens > n - rows:
        return 
    if queens == 0:
        result += 1
        return
    if rows == n:
        return 
    
    for c in range(n):
        if c in col or (rows + c) in posDiag or (rows - c) in negDiag:
            continue
        
        col.add(c)
        posDiag.add(rows + c)
        negDiag.add(rows - c)

        solve(rows + 1, queens - 1)
        
        col.remove(c)
        posDiag.remove(rows + c)
        negDiag.remove(rows - c)
        
    solve(rows + 1, queens)
      

        
solve(0, m)
print(result)
