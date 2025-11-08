
n, k = map(int, input().split())
results = []

def backtrack(start, path):
    if len(path) == k:
        results.append(path[:])
        return

    for nums in range(start, n + 1):
        path.append(nums)
        backtrack(nums + 1, path)
        path.pop()
        
    
    
backtrack(1, [])
print(results)