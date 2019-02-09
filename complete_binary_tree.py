V = int(input())

heap = [0] + list(map(int, input().split()))
for i in range(1, V+1):
    r = 'node{}: key = {}, '.format(i, heap[i])
    parent = i // 2
    r += 'parent key = {}, '.format(heap[parent]) if parent >= 1 else ''
    left = 2 * i
    r += 'left key = {}, '.format(heap[left]) if left < len(heap) else ''
    right = 2 * i + 1
    r += 'right key = {}'.format(heap[right]) if right < len(heap) else ''
    print(r)
