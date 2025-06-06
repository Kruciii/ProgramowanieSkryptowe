from tkinter import *
from tkinter import messagebox
#Napisz program z interfejsem graficznym, który oblicza pole i obwód trójkąta.
#Program powinien zawierać pięć etykiet (Podaj a:, Podaj b:, Podaj c:, Pole:, Obwód:), trzy
#pola tekstowe (do wprowadzania danych), dwa pola tekstowe, w których pojawiać się będą
#wyniki oraz dwa przyciski OBLICZ POLE oraz OBLICZ OBWÓD. Do obliczania pola
#zastosować wzór Herona. Zabezpieczyć program przed nieodpowiednimi danymi, używając
#okien dialogowych. Zadbać o odpowiednie rozmieszczenie widżetów na siatce (manager
#grid()) oraz dobrać odpowiednią kolorystykę. 
class ZaMalaError(Exception):
    pass
class Trojkat(Exception):
    pass
class Konwerter(object):
    def __init__(self):
        self.okno = Tk()
        self.okno.title("Konwerter C-F")
        self.okno.geometry("220x500")
        self.okno.config(background="pink")
        self.buduj()
        self.okno.mainloop()
        
        
    def buduj(self):
        #Etykiety
        self.e1 = Label(self.okno)
        self.e1["text"] = "Podaj a"
        self.e1.grid(row=0,column=0,sticky="W")
        self.e2 = Label(self.okno)
        self.e2["text"] = "Podaj b"
        self.e2.grid(row=2,column=0,sticky="W")
        self.e3 = Label(self.okno)
        self.e3["text"] = "Podaj c"
        self.e3.grid(row=5,column=0,sticky="W")
        self.e4 = Label(self.okno)
        self.e4["text"] = "Pole trójkąta:"
        self.e4.grid(row=8,column=0,sticky="W")
        self.e5 = Label(self.okno)
        self.e5["text"] = "Obwód trójkąta:"
        self.e5.grid(row=10,column=0,sticky="W")
        #Pola
        self.p1 = Entry(self.okno,width=8)
        self.p1.grid(row = 1 ,column = 0, sticky= "W")
        self.p2 = Entry(self.okno,width=8)
        self.p2.grid(row = 3 ,column = 0, sticky= "W")
        self.p3 = Entry(self.okno,width=8)
        self.p3.grid(row = 6 ,column = 0, sticky= "W")
        self.p4 = Entry(self.okno,width=8)
        self.p4.grid(row = 9 ,column = 0, sticky= "W")
        self.p5 = Entry(self.okno,width=8)
        self.p5.grid(row = 11 ,column = 0, sticky= "W")
        #Przycisk
        self.b1 = Button(self.okno, width= 10)
        self.b1["text"]= "Oblicz"
        self.b1["command"]=self.oblicz
        self.b1.grid(row = 7,column=0, sticky= "W")
        
        
  
    def oblicz(self):
        try:
            if(a+b>c and a+c>b and c+b>a):
                a = float(self.p1.get())
                b = float(self.p2.get())
                c = float(self.p3.get())
            else:
                raise Trojkat
            
            if(a<=0 or b<=0 or c<=0):
                raise ZaMalaError
        except ValueError:
             messagebox.showerror("Błąd formatu","kolego wpisałes cos co nie jest liczba będzie klepa")
        except ZaMalaError:
            messagebox.showerror("Błąd wartości","Wpisałes ujemne wartości")
        except Trojkat:
            messagebox.showerror("Błąd wartości","trojkata nie da sie z tego zrobic")
        else:
                
            obwod  = a+b+c
            p= obwod/2
            P = (p * (p - a) * (p - b) * (p - c))**(1/2)   
            self.p4.delete(0,END)
            self.p4.insert(0,P)
            self.p5.delete(0,END)
            self.p5.insert(0,obwod)
        
k=Konwerter()

'''
        self.polewejsciowe = Entry(self.okno, width=8)
        self.polewejsciowe.grid(row = 0,column = 1,sticky="W")
        self.przycisk = Button(self.okno, width= 10)
        self.przycisk["text"]= "Konwertuj"
        self.przycisk["command"] = self.przelicz #Bez nawiasów!
        self.przycisk.grid(row=1,column=0)
        self.etykietawysciowa = Label(self.okno)
        self.etykietawysciowa["text"] = "Oto Temperatura w F: "
        self.etykietawysciowa.grid(row=2,column=0,sticky="W")
        self.polewyj = Entry(self.okno,width=8)
        self.polewyj.grid(row=2,column = 1,sticky ="W")'''