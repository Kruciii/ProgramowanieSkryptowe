import tkinter
from tkinter import messagebox

class UjemnaError(Exception):
    pass

class Kantor:
    def __init__(self):
        self.okno = tkinter.Tk()
        self.okno.title("Kantor")
        self.okno.geometry("300x300")
        self.okno.config(background="lightpink")
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

       
    def calculate(self):
        try:
            # Pobranie wartości z pola
            x = self.p1.get().strip()
            
            if not x:  # Sprawdzenie, czy pole jest puste
                raise ValueError("Pole nie może być puste")
            
            x = float(x.replace(",", "."))  # Konwersja na liczbę
            if x <= 0:
                raise UjemnaError
            
            if x > 10**10:  # Sprawdzenie, czy liczba nie jest za duża
                raise ValueError("Podana liczba jest za duża")
            # Odblokowanie pól tekstowych
            for i in (self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9):
                i.config(state="normal")

            # Usuwanie zawartości pól
            self.p2.delete("1.0", tkinter.END)
            self.p3.delete("1.0", tkinter.END)
            self.p4.delete("1.0", tkinter.END)
            self.p5.delete("1.0", tkinter.END)
            self.p6.delete("1.0", tkinter.END)
            self.p7.delete("1.0", tkinter.END)
            self.p8.delete("1.0", tkinter.END)
            self.p9.delete("1.0", tkinter.END)

            # Wstawianie wyników
            self.p2.insert("1.0", str(round(x / self.USD, 2)))
            self.p3.insert("1.0", str(round(x / self.EUR, 2)))
            self.p4.insert("1.0", str(round(x / self.GBP, 2)))
            self.p5.insert("1.0", str(round(x / self.CHF, 2)))
            self.p6.insert("1.0", str(round(x / self.CZK, 2)))
            self.p7.insert("1.0", str(round(x / self.RUB, 2)))
            self.p8.insert("1.0", str(round(x / self.JPY, 2)))
            self.p9.insert("1.0", str(round(x / self.AUD, 2)))

            # Zablokowanie pól tekstowych
            for i in (self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9):
                i.config(state="disabled")

        except UjemnaError:
            messagebox.showerror("Błąd wartości", "Proszę podać liczbę dodatnią")
            self.p1.delete(0, tkinter.END)  
        except ValueError as ve:
            messagebox.showerror("Błąd wartości", str(ve))
            self.p1.delete(0, tkinter.END)  
        except Exception as e:
            messagebox.showerror("Inny błąd", str(e))


    def build(self):
        
        #Etykiety
        self.e1 = tkinter.Label(self.okno, text="Witaj w kantorze!", bg="white")
        self.e1.grid(row=0, column=0, pady=10,padx = (4,0))
        self.e2 = tkinter.Label(self.okno, text="Wpisz walute w PLN")
        self.e2.grid(row=1, column=1, sticky="W", pady=1)
        self.e3 = tkinter.Label(self.okno, text="USD")
        self.e3.grid(row=2, column=1, sticky="W", pady=1)
        self.e4 = tkinter.Label(self.okno, text="EUR")
        self.e4.grid(row=3, column=1, sticky="W", pady=1)
        self.e5 = tkinter.Label(self.okno, text="GBP")
        self.e5.grid(row=4, column=1, sticky="W", pady=1)
        self.e6 = tkinter.Label(self.okno, text="CHF")
        self.e6.grid(row=5, column=1, sticky="W", pady=1)
        self.e7 = tkinter.Label(self.okno, text="CZK")
        self.e7.grid(row=6, column=1, sticky="W", pady=1)
        self.e8 = tkinter.Label(self.okno, text="RUB")
        self.e8.grid(row=7, column=1, sticky="W", pady=1)
        self.e9 = tkinter.Label(self.okno, text="JPY")
        self.e9.grid(row=8, column=1, sticky="W", pady=1)
        self.e10 = tkinter.Label(self.okno, text="AUD")
        self.e10.grid(row=9, column=1, sticky="W", pady=1)
        

        
        #Entry i Text dla wartości walut
        self.p1 = tkinter.Entry(self.okno,width=10)
        self.p1.grid(row =1, column =0,sticky = "W", pady = 1 ,padx = (4,0))
        self.p2 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p2.grid(row=2, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        self.p3 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p3.grid(row=3, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        self.p4 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p4.grid(row=4, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        self.p5 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p5.grid(row=5, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        self.p6 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p6.grid(row=6, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        self.p7 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p7.grid(row=7, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        self.p8 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p8.grid(row=8, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        self.p9 = tkinter.Text(self.okno, width=10, height=1, wrap="word")
        self.p9.grid(row=9, column=0, sticky = "W", pady = 1 ,padx = (4,0))
        
        #Zablokowanie pól tekstowych
        for i in (self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9):
            i.config(state="disabled")
        #Przyciski
        self.b1 = tkinter.Button(self.okno, width=10)
        self.b1["text"] = "Oblicz"
        self.b1["command"] = self.calculate
        self.b1.grid(row=10, column=0, padx=10, pady=10)  

        self.b2 = tkinter.Button(self.okno, width=10)
        self.b2["text"] = "Zamknij"
        self.b2["command"] = self.okno.destroy
        self.b2.grid(row=10, column=1, padx=10, pady=10) 
        
        self.b3 = tkinter.Button(self.okno, width=6)
        self.b3.grid(row=10, column=2, sticky="E", padx=10, pady=10)
        self.b3["text"] = "Pomoc"
        self.b3["command"] = lambda: messagebox.showinfo("Pomoc", "Wprowadź kwotę w PLN, a następnie naciśnij 'calculate', aby uzyskać przeliczone wartości w innych walutach.")
        
        
            
k=Kantor()