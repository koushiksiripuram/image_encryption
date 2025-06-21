p=61
q=53

n=p*q

pin=(p-1)*(q-1)

e=17
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(e, pin):
    gcd, x, y = extended_euclidean(e, pin)
    if gcd != 1:
        return None
    else:
        return x % pin

d = mod_inverse(e, pin)

def encryption(m):
    em=pow(m,e,n)
    return em

def decryption(dm):
    dcm=pow(dm,d,n)
    return dcm


f=encryption(4)
g=decryption(f)
print(g)