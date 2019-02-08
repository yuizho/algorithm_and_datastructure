class Node:
    def __init__(self, key):
        self.parent = None
        self.key = key
        self.left = None
        self.right = None


    def insert(self, node):
        x = self
        p = self.parent
        while x is not None:
            p = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = p

        if p is None:
            self.parent = node
        elif node.key < p.key:
            p.left = node
        else:
            p.right = node

    def isContains(self, key):
        x = self
        while x is not None:
            if x.key == key:
                return True
            else:
                if key < x.key:
                    x = x.left
                else:
                    x = x.right
        return False


def printNodes(node):
    print(' '.join(inOrder(node)))
    print(' '.join(preOrder(node)))


def preOrder(node, result=[]):
    if node is None:
        return result
    result.append(str(node.key))
    preOrder(node.left, result)
    preOrder(node.right, result)
    return result


def inOrder(node, result=[]):
    if node is None:
        return result
    inOrder(node.left, result)
    result.append(str(node.key))
    inOrder(node.right, result)
    return result


V = int(input())
node = None
for i in range(V):
    command = input()
    if command.startswith('insert'):
        key = int(command.split()[1])
        if node is None:
            node = Node(key)
        else:
            node.insert(Node(key))
    elif command.startswith('find'):
        key = int(command.split()[1])
        if node is None:
            print("no")
        else:
            print("yes") if node.isContains(key) else print("no")
    else:
        printNodes(node)
