x = input().strip()

try:
    interger = int(x)
    print(f"{interger:05d}")

except ValueError:
    try:
        front, back = x.split('.')
        total = len(front) + len(back)
        if total < 5:
            back = back.ljust(5 - len(front), '0')
            
        print(front + '.' + back)
        
    except ValueError:
        print("not a number")