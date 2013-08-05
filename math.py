# exponentiation by repeated squaring, O(log(exponent))
def exp(base,exponent):
    result = 1
    while (exponent > 0):
        if (exponent % 2 == 1):
            result = (result * base)
        exponent /= 2
        base = (base * base)
    return result

'''
n choose k
'''
def nCk(n,k):
    r = 1
    if k > n-k: k = n-k
    for i in xrange(1,k+1):
        r = (r*(n-k+i))/i;
    return r
