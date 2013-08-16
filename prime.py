'''
class to build a list of all primes
below n using sieve of Eratosthenes
'''
class primes():
    def __init__(self,n):
        self.N = n/2
        self.primes = bytearray(b'1'*self.N)
        i = 1
        while i*i <= self.N+1:
            if self.primes[i] == 49:
                for j in xrange(2*i*(i+1), self.N, 2*i+1):
                    self.primes[j]=48
            i += 1
    def isprime(self,p):
        if p/2 > self.N : raise ValueError
        return p==2 or ( p>2 and p%2 != 0 and self.primes[p/2]==49)

    def __iter__(self):
        yield 2
        for i in xrange(1,self.N):
            if self.primes[i]==49: yield 2*i+1

'''
    e.g.1
    from projecteuler import prime
    p = primes(1000)
    for i in p: print i  #prints all primes < 1000
    p.isprime(153)  # tests a number (<1000) is prime or not
'''
