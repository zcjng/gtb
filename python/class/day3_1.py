x = input()
n, m = map(int, x.split())
## 180 420

cowboyLegs = n * 2
horseLegs = m - cowboyLegs

cowboyCount = 0
horseCount = 0

while(cowboyLegs > 0 or horseLegs > 0):
    if(cowboyLegs % 2 == 0):
        cowboyLegs -= 2
        cowboyCount += 1
    if(horseLegs % 4 == 0):
        horseLegs -= 4
        horseCount += 1
         
print(cowboyCount, horseCount)



