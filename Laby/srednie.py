def arytmetyczna(a):
    suma =0
    for i in range(2,len(2,len(a))):
        suma += float(a[i])
    return suma/(len(a)-2)
def geometryczna(a):
    iloczyn =0
    for i in range(2,len(2,len(a))):
        iloczyn *= float(a[i])
    return iloczyn**(1/(len(a)-2))
def harmoniczna(a):
    suma =0
    for i in range(2,len(a)):
        suma+= 1/float(a[i])
    return (len(a)-2)/suma

if __name__ =="__main__":
    print("to tylko modul")

