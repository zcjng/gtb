def cal(a, b, c, d):
    return a * b * c + d

H = int(input())
count = 0
for a in range(1, H+1):
    for b in range(1, H+1):
        for c in range(1, H+1):
            for d in range(1, H+1):
                if cal(a, b, c, d) == H:
                    count += 1
print(count)
