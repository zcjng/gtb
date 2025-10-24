from collections import Counter

s = 'racecar'
t = 'carrace'

sCount = Counter(s)
tCount = Counter(t)

if sCount == tCount:
    print(True)
else:
    print(False)
