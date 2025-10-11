def count_quadruples(H):
    count = 0
    
    for a in range(1, H + 1):
        for b in range(1, H // a + 1):
            max_c = (H - 1) // (a * b)
            if max_c > 0:
                count += max_c
    
    return count

H = int(input())
print(count_quadruples(H))