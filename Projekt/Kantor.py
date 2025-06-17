import tkinter
from tkinter import messagebox
class UjemnaError(Exception):
    pass

class Kantor:
    def __init__(self):
        self.okno = tkinter.Tk()
        self.okno.title("Kantor")
        self.okno.geometry("400x700")
        self.okno.config(background="lightblue")
        self.build()
        self.USD = 4.0
        self.EUR = 4.5
        self.GBP = 5.0
        self.CHF = 4.2
        self.CZK = 0.18
        self.RUB = 0.05
        self.JPY = 0.03
        self.AUD = 2.8
        self.okno.mainloop()

       
    def oblicz(self):
        try:
            x = float(self.p1.get())
            if(x<=0):
                raise UjemnaError
            
            self.p2.delete(0,tkinter.END)
            self.p3.delete(0,tkinter.END)
            self.p4.delete(0,tkinter.END)
            self.p5.delete(0,tkinter.END)
            self.p6.delete(0,tkinter.END) 
            self.p7.delete(0,tkinter.END)
            self.p8.delete(0,tkinter.END)
            self.p9.delete(0,tkinter.END)
            self.p2.insert(0,round(x/self.USD,2))
            self.p3.insert(0,round(x/self.EUR,2))
            self.p4.insert(0,round(x/self.GBP,2))
            self.p5.insert(0,round(x/self.CHF,2))
            self.p6.insert(0,round(x/self.CZK,2))
            self.p7.insert(0,round(x/self.RUB,2))
            self.p8.insert(0,round(x/self.JPY,2))
            self.p9.insert(0,round(x/self.AUD,2))
        except UjemnaError:
            messagebox.showerror("Błąd wartośći","Proszę podać liczbę dodatnią")
        except TypeError:
            messagebox.showerror("Błąd typu","Proszę podać dane będące liczbą")
        except ValueError:
            messagebox.showerror("Błąd wartości","Proszę podać liczbę")
        except Exception as e:
            messagebox.showerror("Inny błąd",e)


    def build(self):
        self.e1 = tkinter.Label(self.okno, text="Witaj w kantorze!", bg="blue")
        self.e1.grid(row=0, column=0, pady=10)
        self.e2 = tkinter.Label(self.okno,text= "Wpisz walute w PLN")
        self.e2.grid(row = 1,column = 1,sticky="W")
        self.e3 = tkinter.Label(self.okno,text= "USD")
        self.e3.grid(row = 2,column = 1,sticky="W")
        self.e4 = tkinter.Label(self.okno,text= "EUR")
        self.e4.grid(row = 3,column = 1,sticky="W")
        self.e5 = tkinter.Label(self.okno,text= "GBP")
        self.e5.grid(row = 4,column = 1,sticky="W")
        self.e6 = tkinter.Label(self.okno,text= "CHF")
        self.e6.grid(row = 5,column = 1,sticky="W")
        self.e7 = tkinter.Label(self.okno,text= "CZK")
        self.e7.grid(row = 6,column = 1,sticky="W")
        self.e8 = tkinter.Label(self.okno,text= "RUB")
        self.e8.grid(row = 7,column = 1,sticky="W")
        self.e9 = tkinter.Label(self.okno,text= "JPY")
        self.e9.grid(row = 8,column = 1,sticky="W")
        self.e10 = tkinter.Label(self.okno,text= "AUD")
        self.e10.grid(row = 9,column = 1,sticky="W")
        
        
        
        self.p1 = tkinter.Entry(self.okno,width=10)
        self.p1.grid(row =1, column =0,sticky = "W")
        self.p2 = tkinter.Entry(self.okno)
        self.p2.grid(row =2,column = 0,sticky = "W")
        self.p3 = tkinter.Entry(self.okno)
        self.p3.grid(row =3,column = 0,sticky = "W")
        self.p4 = tkinter.Entry(self.okno)
        self.p4.grid(row =4,column = 0,sticky = "W")
        self.p5 = tkinter.Entry(self.okno)
        self.p5.grid(row =5,column = 0,sticky = "W")
        self.p6 = tkinter.Entry(self.okno)
        self.p6.grid(row =6,column = 0,sticky = "W")
        self.p7 = tkinter.Entry(self.okno)
        self.p7.grid(row =7,column = 0,sticky = "W")
        self.p8 = tkinter.Entry(self.okno)
        self.p8.grid(row =8,column = 0,sticky = "W")
        self.p9 = tkinter.Entry(self.okno)
        self.p9.grid(row =9,column = 0,sticky = "W")
        
        
        self.b1 = tkinter.Button(self.okno, width = 10)
        self.b1["text"] = "oblicz"
        self.b1["command"] = self.oblicz
        self.b1.grid(row = 10,column = 1)
        self.b2 = tkinter.Button(self.okno, width=10)
        self.b2["text"] = "zamknij"
        self.b2["command"] = self.okno.destroy
        self.b2.grid(row=10, column=2)
   
            
k=Kantor()