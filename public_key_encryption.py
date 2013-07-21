#! /usr/bin/env python
#
#   demo for a public key encryption
#   8-bit RSA
#
def egcd(a,b):
    if b==0: return (1,0,a)
    x,y,d = egcd(b,a%b)
    return (y,x-(a/b)*y,d)

# key-gen
# generate 2 primes p,q
# pick e such that its coprime with (p-1)*q(-1)
# public_key = p*q, e
#privete)key = modulo multiplicative inverse of e mod (p-1)*(q-1)
p,q = 13,17
N = p*q
e = 13
#Bob's public key
#available to everyone
#used for encryption
public_key = N,e
#Bob's private key
#available only to Bob
#used for decryption
private_key = egcd((p-1)*(q-1),e)[1]%((p-1)*(q-1))

def encode(message):
    return [ord(c) for c in message]
def decode(message):
    return ''.join([chr(c) for c in message])

def encrypt(plaintext):
    return [pow(p,public_key[1],public_key[0])
                for p in encode(plaintext)]
def decrypt(ciphertext):
    return [pow(c,private_key,public_key[0])
                for c in ciphertext]


mess = 'The more I see, the less I Know, the more I want to let it go.Hey Oh!'
print 'Original Message:', mess
print 'Alice sends encrypted Message:',decode(encrypt(mess))
print 'Eve sees encypted Message:',decode(encrypt(mess))
print 'Bob gets and decodes with his private key:',decode(decrypt(encrypt(mess)))
