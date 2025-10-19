nums = list(map(int, input().split()))


tree = []

def permutate(path):
    if len(path) == len(nums):
        tree.append(path[:])
        return

    for index in nums:
        if index in path:
            continue
        
        path.append(index)
        permutate(path)
        path.pop()
        
        

permutate([])
print(tree)