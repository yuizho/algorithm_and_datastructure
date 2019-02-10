n = int(input())
cache = [-1]*(n+1)

def fibo(n):
    if n == 0 or n == 1:
        cache[n] = 1
        return cache[n]
    if cache[n] != -1:
        return cache[n]
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]


print(fibo(n))
