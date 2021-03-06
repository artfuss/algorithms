from math import sqrt
#
#   sum of all divisors of n
#   http://mathforum.org/library/drmath/view/71550.html
#   e.g. 15 = 24 {1 + 3 + 5 + 15}
#   O(sqrt(n))
#
def sum_of_divisors(n):
    res = 1
    for i in xrange(2,int(sqrt(n))+1):
        j=1
        while n%i == 0:
            j += 1
            n /= i
        res *= ((i**j-1)/(i-1))
    if n != 0 : res *= (n+1)
    return res

#
#   number of all divisors of n
#   e.g. 15 = 4 {1,3,5,15}
#   O(sqrt(n))
#
def num_of_divisors(n):
    if n==1: return 1
    res = 1
    for i in xrange(2,int(sqrt(n))+1):
        j=0
        while n%i == 0:
            j += 1
            n /= i
        res *= (j+1)
    if n > 1: res *= 2
    return res

# list of divisors of a number n, O(sqrt(n))
def divisors(n):
    facts = []
    i = 1
    while i*i <= n:
        if n%i ==0:
            facts.append(i)
            if i*i != n:
                facts.append(n/i)
        i += 1
    return facts
