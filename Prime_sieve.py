def prime_sieve(n):
    k = list(range(2,n))
    for i in k:
        j = 2
        while j < k[::-1][0]:
            if i*j in k:
                k.remove(i*j)
            j += 1
    return k
