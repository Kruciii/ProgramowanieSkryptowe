napis = input("podaj napis:")
pusty=""
for i in napis:
    if i.lower() =="a":
        pusty+="7"
    elif i.lower() =="d":
        pusty+="1"
    elif i.lower() =="d":
        pusty+="1"
    else:
        pusty+=i
        
print("zaszyfrowana wiadomość")