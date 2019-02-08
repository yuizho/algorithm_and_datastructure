class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
        self.depth = 0

        
def calc_depth(nodes, node_id, arg_depth):
    #print(nodes[node_id].right)
    nodes[node_id].depth = arg_depth

    if nodes[node_id].left is not -1:
        calc_depth(nodes, nodes[node_id].left, arg_depth+1)
    if nodes[node_id].right is not -1:
        calc_depth(nodes, nodes[node_id].right, arg_depth+1)


V = int(input())

nodes = []
for loop in range(V):
    node = Node()
    nodes.append(node)

for n in range(V):
    node_id, left, right = map(int, input().split())
    nodes[n].left = left
    nodes[n].right = right
    if left is not -1:
        nodes[left].parent = n
    if right is not -1:
        nodes[right].parent = n

calc_depth(nodes, 0, 0)


for i in range(V):
    print("node %d: parent = %d, depth = %d, "%(i,nodes[i].parent,nodes[i].depth))
