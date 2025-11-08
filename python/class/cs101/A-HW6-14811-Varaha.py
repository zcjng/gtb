items = {}

# Functions
def add():
    item, value = input().split()
    value = int(value)
    items[item] = items.get(item, 0) + value

def remove():
    item, value = input().split()
    value = int(value)
    if item in items:
        items[item] -= value
        if items[item] <= 0:
            del items[item]

def count():
    count = 0
    for i in items.values():
        count += i
    print(count)


# Command mapping using lambdas
actions = {
    'add': add,
    'remove': remove,
    'show': lambda: print(items),
    'count': count,
    'clear': lambda: items.clear()
    
}

# Main program
n = int(input())
for _ in range(n):
    cmd = input().strip()
    actions[cmd]()
    # todo