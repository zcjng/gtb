s = input()
slicing = input()
x, y = map(int, slicing.split())


print(s[:x]+s[(y+1):]+s[x:(y+1)])
