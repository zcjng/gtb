import ast

dirCounter = 0
tree = ast.literal_eval(input().strip())
currentDir = tree[0]

def time_machine(parent, currentDir):
    for child in parent[1:]:
        if isinstance(child, list):
            time_machine(child, currentDir + '/' + child[0])
        else:
            print("Deleting /" + currentDir + '/' + child)
    
    print('Deleting /' + currentDir)
            
            
            


time_machine(tree, currentDir)

