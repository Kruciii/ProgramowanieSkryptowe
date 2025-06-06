pizze = {"americana":35 , "capriciossa" : 38, "wegetariańska":29}
sosy = {"pomidorowy":5,"czosnkowy":6}
napoje = {"cola":9,"fanta":8,"sprite":7}

def zamowienie():
    p = input("WYBIERZ PIZZUNIE")
    s = input("JAKIE SOSIWO WARIACIE")
    n = input("Wybierz napoj cola/fanta/sprite")
    return (p,s,n)
def rachunek():
    p,s,n = zamowienie()
    return pizze[p]+sosy[s]+napoje[n]

if __name__ =="__main__":
    print("To jest tylko moduł mordeczko")