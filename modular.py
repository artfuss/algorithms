MOD = 25

#extended euclid gcd
def egcd(a,b):
    if b==0: return (1,0,a)
    x,y,d = egcd(b,a%b)
    return (y,x-(a/b)*y,d)

def add(a,b):
    return (a+b)%MOD
def sub(a,b):
    return (a-b)%MOD
def mul(a,b):
    return (a*b)%MOD
#only if b and MOD are coprime
#modulo multiplicative inverse
def div(a,b):
    return mul(a,egcd(MOD,b)[1])
def exp(a,b):
    return pow(a,b,MOD)
