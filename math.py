# exponentiation by repeated squaring, O(log(exponent))
def exp(base,exponent):
    result = 1
    while (exponent > 0):
        if (exponent % 2 == 1):
            result = (result * base)
        exponent /= 2
        base = (base * base)
    return result
    
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
