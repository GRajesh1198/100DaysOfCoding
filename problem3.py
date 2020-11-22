def primes(n):
    isPrime=[False] * 2 + [True] * (n-1)
    for x in range(n):
        if isPrime[x]:
            for i in range(2 * x,n,x):
                isPrime[x]=False
    for i in range(n):
        if isPrime[i]:
            print(i)
primes(30)

