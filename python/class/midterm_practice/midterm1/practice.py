def hanoi(n, start, end):
    if n == 1:
        move(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        move(start, end)
        hanoi(n - 1, other, end)
        
def move(start, end):
    print(f"{start} -> {end}")
    
n = int(input('Input the n: '))
start, end = map(int, input('From where to start and end: ').split())
hanoi(n, start, end)