# exponentiation by repeated squaring, O(log(exponent))
def exp(base,exponent):
    result = 1
    while (exponent > 0):
        if (exponent % 2 == 1):
            result = (result * base)
        exponent /= 2
        base = (base * base)
    return result
