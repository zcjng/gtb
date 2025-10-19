from ast import literal_eval

def gen(tree: tuple):
    parent, children = tree
    yield parent
    for child in children:
        yield from gen(child)
        
genVar = gen(literal_eval(input()))
while True:
    try:
        print(next(genVar))
    except StopIteration:
        break