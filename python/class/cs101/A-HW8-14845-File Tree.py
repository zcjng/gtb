import sys

class Node:
    def __init__(self, name, is_dir, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = {}

class FileTree:
    def __init__(self):
        self.root = Node("/", True, None)
        self.cwd = self.root
   
    # !!! You can add more functions if needed !!! #
   
    def path_to_nodes(self, path):
        # TODO
        if path == '.':
            current = self.cwd
            nodes = []
            while current is not None:
                nodes.append(current)
                current = current.parent
            return nodes[::-1]

        if path.startswith('/'):
            current = self.cwd
            nodes = [self.cwd]
            path = path[1:]
        else:
            current = self.cwd
            nodes = []
            while current is not None:
                nodes.append(current)
                current = current.parent
            nodes = nodes[::-1]
            current = self.cwd

        if not path:
            return nodes

        parts = path.split('/')

        for part in parts:
            if part == " " or part == '.':
                continue
            elif part == "..":
                if current.parent:
                    current = current.parent
                    nodes.pop()
                else:
                    return None
            else:
                if part in current.children:
                    current = current.children[part]
                    nodes.append(current)
                else:
                    return None
        return nodes
    def mkdir(self, path):
        if path.endswith('/') and len(path) > 1:
            path = path[:-1]
        idx = path.rfind('/')
        if idx == -1:
            p_path, name = ".", path
        elif idx == 0:
            p_path, name = "/", path[1:]
        else:
            p_path, name = path[:idx], path[idx+1:]
        nodes = self.path_to_nodes(p_path)
        if nodes:
            parent = nodes[-1]
            if parent.is_dir and name not in parent.children:
                parent.children[name] = Node(name, True, parent)

    def cd(self, path):
        # TODO
        nodes = self.path_to_nodes(path)
        target = nodes[-1]
        if target.is_dir:
            self.cwd = target

    def ls(self):
        # TODO
        print(" ".join(sorted(self.cwd.children.keys())))

    def touch(self, path):
        if path.endswith('/') and len(path) > 1:
            path = path[:-1]
        idx = path.rfind('/')
        if idx == -1:
            p_path, name = ".", path
        elif idx == 0:
            p_path, name = "/", path[1:]
        else:
            p_path, name = path[:idx], path[idx+1:]
        nodes = self.path_to_nodes(p_path)
        if nodes:
            parent = nodes[-1]
            if parent.is_dir and name not in parent.children:
                parent.children[name] = Node(name, False, parent)
        

    def rm(self, path):
        # TODO
        if path.endswith('/') and len(path) > 1:
            path = path[:-1]
        idx = path.rfind('/')
        if idx == -1:
            p_path, name = ".", path
        elif idx == 0:
            p_path, name = "/", path[1:]
        else:
            p_path, name = path[:idx], path[idx+1:]
        nodes = self.path_to_nodes(p_path)
        if nodes:
            parent = nodes[-1]
            if parent.is_dir and name in parent.children:
                target = parent.children[name]
                if not target.is_dir:
                    del parent.children[name]
    # Debug functions
    def print_prompt(self):
        nodes = self.path_to_nodes(".")
        path_str = "/" + "/".join([n.name for n in nodes[1:]])
        if path_str.endswith("/") and len(path_str) > 1: path_str = path_str[:-1]
        print(f"{path_str} >", end=" ", flush=True)

    def print_all(self, node=None, prefix=""):
        if node is None: node, prefix = self.root, ""
        current = prefix + ("/" + node.name if node != self.root else "")
        print(current if node.is_dir else f"{current} (file)")
        if node.is_dir:
            for k in sorted(node.children): self.print_all(node.children[k], current)

def main():
    ft = FileTree()
    # !!! Enable debug mode here !!!
    # !!! Remember to disable it when submitting !!!
    DEBUG_MODE = True
    
    while True:
        if DEBUG_MODE: ft.print_prompt()
        try:
            line = sys.stdin.readline()
            if not line:
                if DEBUG_MODE: print()
                break
        except: break

        line = line.strip()
        if not line: continue

        p = line.split()
        cmd, args = p[0], p[1:]

        if   cmd == 'mkdir' and len(args)==1: ft.mkdir(args[0])
        elif cmd == 'cd'    and len(args)==1: ft.cd(args[0])
        elif cmd == 'ls'    and len(args)==0: ft.ls()
        elif cmd == 'touch' and len(args)==1: ft.touch(args[0])
        elif cmd == 'rm'    and len(args)==1: ft.rm(args[0])
        elif cmd == 'print_all':              ft.print_all()

        if DEBUG_MODE and cmd != 'ls':
            print("--- Tree ---"); ft.print_all(); print("------------")

if __name__ == "__main__":
    main()
