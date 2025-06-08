def usun12(l)
    nowy =""
    try:
        if(not isinstance(l,str)):
            raise TypeError
        if len(l) == 0
            raise ValueError
        for i in l:
            if(i!="1" or i!="2)
                nowy +=i
    except TypeError:
        print("Zmienna przekazana do funkcji nie jest str")
    except ValueError:
        print("Zmienna przekazana do funckji ma długość 0")
    except Exception as e:
        print("inny blad:",e)

def liczbasamoglosek(l):
    samogloski = "aeiouąęió"
    liczba =0
    try:
        if(not isinstance(l,str))
            
