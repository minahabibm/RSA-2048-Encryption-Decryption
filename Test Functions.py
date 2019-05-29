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
    Q = sympy.randprime(10,100)
    P = sympy.randprime(10,20)
    if(Q != P): #test cases will be Q + P - 1 = 2 + 2 - 1 = 3 digits ex. 101
        break

n = Q * P
phi = (Q-1) * (P-1)
e = 17 #3,5,17,257,65537
d = multiplicative_inverse(e, phi)

print("Modulo")
print(n)
print("public Key")
print(e)
print("private Key")
print(d)

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
#########################################################################################################################
#program to test code RSA encryption algorithm
f = open("IMG_3404.jpeg","rb") #to specify a file to be opened.
s = f.read()
f.close()

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []

for c in s:   # in Python, a string is just a sequence, so we can iterate over it!
    l1.append(c)
    #l2.append(ord(chr(c)))
    #l2.append(c)

r = input("Enter Modulo: ")
t = input("Enter Public Key: ")

for x in l1:
    l3.append(Encryption(int(x), int(t), int(r)))

fo = open("Encrypted File","w")
for x in l3:
    fo.write(str(x)+"\n")
fo.close
#########################################################################################################################
u = input("Enter Private Key For Decryption: ")

fr = open("Encrypted File","r") #Function to read to list
fi = fr.readlines()
for y in fi:
    currentPlace = y[:-1]
    l5.append(int(currentPlace))
fr.close

for y in l5: #l3 to read from a list, l5 to read from a file
    l4.append(Decryption(int(y), int(u), int(r)))

fi = open("Decrypted File","wb")
for y in l4:
    fi.write(bytes((y,)))
fi.close


#########################################################################################################################
'''
f = open('IMG_3404.jpeg', 'rb') # Funtion to read any file in binary format
fw = open("BINARY","wb")
file_content = f.read()
for y in file_content:
    fw.write(bytes([y]))
f.close()
fw.close()

for z in l4:
    l5.append(z)
    l5.append(chr(z))
print(l5)
Message = "".join(l5)
print(Message)

"Binary" files are any files where the format isn't made up of readable characters. 
Binary files can range from image files like JPEGs or GIFs, audio files like MP3s or binary document formats like Word 
or PDF. In Python, files are opened in text mode by default. To open files in binary mode, when specifying a mode, add 
'b' to it.For example,

f = open('my_file.mp3', 'rb')
file_content = f.read()
f.close()

f = open('IMG_3404.jpeg', 'rb') # Funtion to read any file in binary format
fw = open("BINARY","wb")
file_content = f.read()
for y in file_content:
    print(bytes([y]))
    fw.write(bytes([y]))
f.close()
fw.close()
'''