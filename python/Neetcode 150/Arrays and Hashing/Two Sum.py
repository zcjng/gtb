nums = [2, 5, 5, 11]

target = 10

indices = {}
for i, n in enumerate(nums):
    indices[n] = i
    
for i, n in enumerate(nums):
    difference = target - n
    if difference in indices and indices[difference] != i:
        print([i, indices[difference]])
