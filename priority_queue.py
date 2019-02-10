from heapq import heappush, heappop

heap = []
result = None
while True:
    command = input()
    if command == 'end':
        break
    elif command.startswith('insert'):
        heappush(heap, command.split()[1])
    elif command.startswith('extract'):
        print(heappop(heap))
