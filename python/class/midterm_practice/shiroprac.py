testcases = int(input())

totals = []

for i in range(testcases):
    arrLength = int(input())

    arr = list(map(int, input().split()))
    
    maxSum = -999999
    for i in range(arrLength):
        currSum = 0
        for j in range(i, arrLength):
            currSum += arr[j]
            if currSum > maxSum:
                maxSum = currSum
                
    totals.append(maxSum)
                
            
for i in totals:
    print(i)
    
# Brute Forcing, Time Limit Exceeded because it's time complexity is O(n^2)


testcases = int(input())

totals = []

for _ in range(testcases):
    arrLength = int(input())

    arr = list(map(int, input().split()))
    
    currSum = arr[0]
    maxSum = arr[0]
    
    for i in range(1, arrLength):
        currSum = max(arr[i], currSum + arr[i]) #It checks it self with the index behind
        maxSum = max(maxSum, currSum)           #If the index behind is larger then it extends and becomes a part of the subarray
    totals.append(maxSum)                       #If it's smaller then the currentSum becomes the initial index
                
            
for i in totals:
    print(i)
    
# Kadane's Algorithm