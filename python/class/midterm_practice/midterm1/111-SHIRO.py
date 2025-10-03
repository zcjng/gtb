testcases = int(input())

totals = []

for _ in range(testcases):
    arrLength = int(input())

    arr = list(map(int, input().split()))
    
    currSum = arr[0]
    maxSum = arr[0]
    
    for i in range(1, arrLength):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(maxSum, currSum)
    totals.append(maxSum)
                
            
for i in totals:
    print(i)
    