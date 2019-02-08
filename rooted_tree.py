class Node:
    def __init__(self):
        self.parent_id = -1
        self.depth = 0
        self.children = []


global nodes


def calc_depth(node_id, arg_depth):
    nodes[node_id].depth = arg_depth
    for child in nodes[node_id].children:
        calc_depth(child, arg_depth+1)

V = int(input())

nodes = []
for loop in range(V):
    node = Node()
    nodes.append(node)

for loop in range(V):
    table = list(map(int, input().split()))
    node_id = table[0]
    num = table[1]

    for i in range(num):
        child_id = table[2+i]
        nodes[node_id].children.append(child_id)
        nodes[child_id].parent_id = node_id


calc_depth(0, 0)

for i in range(V):
    print("node %d: parent = %d, depth = %d, "%(i,nodes[i].parent_id,nodes[i].depth))
