num = int(input())

def summ(num):
    if num == 1:
        return 1
    else:
        return num + summ(num - 1)
    
    
print(summ(num))