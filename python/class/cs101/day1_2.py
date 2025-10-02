x = "F-string "
print(f"This is how you use an {x}")

age = 61
distance = "200"
isTeacher = False

if isTeacher:
    print(f"This student was originally a teacher : {isTeacher}")
else:
    print("This student was not originally a teacher") # Python heavily relies on its spacing structure

if 45 < age < 60:
    print(f"This man's age is about middle aged : {age2}")
else:
    print("We don't know this man's age")

print(type(isTeacher))

distance = int(distance)

ratio = distance + age
print(f"The total multiplication is {ratio}")