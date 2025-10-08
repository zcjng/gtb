from collections import Counter

x = input().strip()
y = input().strip()

xCount = Counter(x)
yCount = Counter(y)

minimums = 0

for c in set(xCount) | set(yCount):
    
    minimums += min(xCount[c], yCount[c])

print(len(x) - minimums)



