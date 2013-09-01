# segmented sieve of eratosthenes
# http://stackoverflow.com/questions/10249378/segmented-sieve-of-eratosthenes/10249801#10249801 
from math import sqrt
 
def primes(n):
    ps, sieve = [], [True] * (n)
    for p in range(2, n):
        if sieve[p]:
            ps.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return ps
 
def primesRange(lo, hi, delta):
    def qInit(p): return ((lo + p + 1) / -2) % p
    def qReset(p, q): return (q - delta) % p
    output, sieve = [], [True] * delta
    ps = primes(int(sqrt(hi)))[1:]
    qs = map(qInit, ps)
    while lo < hi:
        for i in range(0, delta):
            sieve[i] = True
        for p, q in zip(ps, qs):
            for i in range(q, delta, p):
                sieve[i] = False
        qs = map(qReset, ps, qs)
        for i, t in zip(range(0, delta), range(lo+1, hi, 2)):
            if sieve[i]: output.append(t)
        lo += (2 * delta)
    return output
 
print primesRange(100, 200, 10)
