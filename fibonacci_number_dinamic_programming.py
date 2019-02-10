N = int(input())


def fibo(n, cache):
    cache[0] = 1
    cache[1] = 1
    for n in range(2, N+1):
        # when cache[n] is calculated,
        # cache[n-1], cache[n-2] was already calculated.
        # it's basic thought of dynamic programming.
        cache[n] = cache[n-1] + cache[n-2]
    return cache


print(fibo(N, [-1]*(N+1))[N])
