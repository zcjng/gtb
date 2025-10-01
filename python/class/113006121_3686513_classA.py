# Cowboy and Horses NTHUOJ

x = input()
y = x.split()
a, b = map(int, y)

aCount = 0
bCount = 0

while b > 0:
    a -= 4
    b -= 1
    bCount += 1

while a > 0:
    a -= 2
    aCount += 1

print(aCount, bCount)


