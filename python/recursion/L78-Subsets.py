nums = list(map(int, input().split()))

result = []
def subset(index, path):
    if index == len(nums):
        result.append(path[:])
        return
    
    path.append(nums[index])
    subset(index + 1, path)
    path.pop()
    
    subset(index + 1, path)
    

subset(0, [])
print(result)
    
    
