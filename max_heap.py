V = int(input())
raw_list = list(map(int, input().split()))

def max_heapfy(L, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(L) and L[left] > L[i]:
        largest = left
    if right < len(L) and L[right] > L[largest]:
        largest = right

    if largest is not i:
        # tmp = L[i]
        # L[i] = L[largest]
        # L[largest] = tmp
        L[i], L[largest] = L[largest], L[i]
        max_heapfy(L, largest)

def build_max_heap(L):
    for i in range((len(L)-1)//2, -1, -1):
        max_heapfy(L, i)


build_max_heap(raw_list)
print(raw_list)
