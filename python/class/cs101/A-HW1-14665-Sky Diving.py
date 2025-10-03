import math

x = input()
y = x.split()
a, b, c= map(int, y)

deltaA = a - 5500   # this becomes C  formula is S = Vot + 1/2at^2
speed = b           # this becomes B            
c *= 0.5            # this becomes A


discriminant = abs(pow(speed, 2) - (4 * deltaA * c))
root1 = (-speed + math.sqrt(discriminant)) / (2*c)
root2 = (-speed - math.sqrt(discriminant)) / (2*c)

root = max(root1, root2)

print(int(root))
