x = input()
xlen = len(x)
total = 0

for i in range(xlen):
    if(i % 2 == 0):
        total += int(x[i])
        
print(total)