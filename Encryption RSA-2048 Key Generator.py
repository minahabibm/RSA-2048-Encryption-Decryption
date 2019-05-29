#RSA-2048 encryption program
#Message Length must be less than or equal P + Q - 1 bits of the RSA.
import sympy

def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx
def Encryption(m, puk, pk):
  return (m ** puk) % pk
def Decryption(Em, prk, pk):
  return (Em ** prk )% pk

while True:
    Q = sympy.randprime(1**1024,10**1024)
    P = sympy.randprime(1**1024,10**1024)
    if (Q != P):
        break
n = Q * P
phi = (Q-1) * (P-1)
e = 65537
d = multiplicative_inverse(e, phi)

fw = open("Modulus","w+")
for x in str(n):
 fw.write(str(x))
fw.close()

fw = open("Public Key","w+")
for y in str(e):
 fw.write(str(y))
fw.close()

fw = open("Private Key","w+")
for z in str(d):
 fw.write(str(z))
fw.close()
