import time

def Decryption(Em, prk, pk):
  return (Em ** prk )% pk

l1 = []
l2 = []
l3 = []

f = open("Encrypted Message","r")
stri = [line.rstrip('\n') for line in f]
f.close()
for x in stri:
    l1.append(x)

n = input("Enter Modulo: ")
d = input("Enter Private Key: ")

start = time.time()

for x in l1:
    l2.append(Decryption(int(x), int(d), int(n)))
for y in l2:
    l3.append(chr(y))
Message = "".join(l3)
print(Message)
fw = open("Decrypted Message","w+")
for z in l3:
 fw.write(str(z))
fw.close()

end = time.time()

print(end - start) # print out the time in seconds