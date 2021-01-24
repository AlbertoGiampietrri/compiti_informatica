n_nazioni=int(input("Quante nazioni vuoi inserire? "))
d={}
contatore=0

while True:
    nazione=input("Inserisci il nome della nazione: ")
    capitale=input("Inserisci il nome della capitale: ")
    d[nazione]=capitale
    contatore+=1
    if contatore == n_nazioni:
        break
    
print()
scelta=input("Inserisci il nome della nazione della quale vuoi sapere la capitale: ")
if scelta in d:
    print(d[scelta])
else:
    print("La nazione scelta non è presente nell'elenco")