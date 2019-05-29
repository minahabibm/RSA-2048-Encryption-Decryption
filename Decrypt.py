def Decryption(Em, prk, pk):
  return (Em ** prk )% pk

l1 = []
l2 = []
l3 = []

choose = input("Enter 1 to decrypt messege from a file ,Or 2 to decrypt a File:  ")
n = input("Enter Modulo: ")
d = input("Enter Private Key: ")

if int(choose) == 1:
    f = open("Encrypted Message","r")
    stri = [line.rstrip('\n') for line in f]
    f.close()
    for x in stri:
        l1.append(x)
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

elif int(choose) == 2:
    f = open("Encrypted Message", "r")  # Function to read to list
    fi = f.readlines()
    for y in fi:
        currentPlace = y[:-1]
        l1.append(int(currentPlace))
    f.close
    for y in l1:  # l3 to read from a list, l5 to read from a file
        l2.append(Decryption(int(y), int(d), int(n)))

    fi = open("Decrypted File", "wb")
    for y in l2:
        fi.write(bytes((y,)))
    fi.close