n_nazioni=int(input("Quante nazioni vuoi inserire? "))
nazioni=[]
capitali=[]
contatore=0

while True:
    nazione=input("Inserisci il nome della nazione: ")
    nazioni.append(nazione)
    capitale=input("Inserisci il nome della capitale: ")
    capitali.append(capitale)
    contatore+=1
    if contatore == n_nazioni:
        break

print()
nazione=input("Inserisci il nome della nazione della quale vuoi sapere la capitale: ")
if nazione in nazioni:
    indice=nazioni.index(nazione)
    print("La capitale della nazione scelta è: ", capitali[indice])
else:
    print("La nazione scelta non è presente nell'elenco")
