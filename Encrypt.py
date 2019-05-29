def Encryption(m, puk, pk):
  return (m ** puk) % pk

choose = input("Enter 1 to write, 2 to select text from file, 3 to select file:  ")

if(int(choose) == 1):
    stri = input("Enter Message To Encrypt:  ")
elif(int(choose) == 2):
   f = open("Message","r")
   stri = f.read()
   f.close()
elif(int(choose) == 3):
    f = open("IMG_3404.jpeg", "rb")  # to specify a file to be opened.
    stri = f.read()
    f.close()
else:
    print("please make a valid choice")

l1 = []
l2 = []

if int(choose) == 1 or int(choose) == 2:
    for c in stri:
        l1.append(ord(c))
elif int(choose) == 3:
    for c in stri:
        l1.append(c)

n = input("Enter Modulo: ")
e = input("Enter Public Key: ")

for x in l1:
    l2.append(Encryption(int(x), int(e), int(n)))

print(l2)
fw = open("Encrypted Message","w+")
for y in l2:
 fw.write(str(y) + "\n")
fw.close()