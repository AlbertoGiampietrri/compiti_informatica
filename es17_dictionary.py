n_capitali=int(input("Quante capitali vuoi inserire? "))
d={}
contatore=0

while True:
    nazione=input("Inserisci il nome della nazione: ")
    capitale=input("Inserisci il nome della capitale: ")
    d[capitale]=nazione
    contatore+=1
    if contatore == n_capitali:
        break

print()
scelta=input("Inserisci il nome della capitale della quale vuoi sapere la nazione: ")
if scelta in d:
    print(d[scelta])
else:
    print("La capitale scelta non è presente nell'elenco")