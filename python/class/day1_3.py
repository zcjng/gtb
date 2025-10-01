import math
'''

x = input("What is your race : ") # the data that is inputted will always be stored as a string type
print(f"Your race is {x}")

numbers = input("Enter two numbers, your age and a random number : ")
number = numbers.split()
a, b = map(int, number)
total = a * b
print(f"This is the number we calculated with your preset numbers {total}")
'''


friends = float(10)
friends /= 3 
print(f"This is how many friends you currently have {round(friends)}")

x = 5
x -= 10
x = pow(x, 2)
print(abs(x))
print(math.sqrt(x))

a = 20
b = 25
c = math.pi
result_max = max(a, b, c)
result_min = min(a, b, c)
print(f"This is the max value {result_max}, and this is the min value {round(result_min, 2)}")

value = input("Enter two numbers for the sides of the triangle : ")
values = value.split()
adj, opp = map(int, values)
result = math.sqrt(pow(adj, 2) + pow(opp, 2))

print(f"The result of the hypotenuse would be {result}")