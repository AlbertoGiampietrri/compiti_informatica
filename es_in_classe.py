prenotazioni={}
prenotazioni_confermate={}

while True:
    partecipante=input("Inserisci il nome del partecipante: ")
    orario=int(input("Inserisci l'orario della prenotazione(solo orari di punta): "))
    prenotazioni[partecipante]=orario
    continuo=int(input("Premi 1 se vuoi continuare, o 2 se non vuoi "))
    if continuo == 1:
        print()
    else:
        break

print()
print("Adesso vedrai ogni prenotazione e potrai decidere se dare la conferma")
for x in prenotazioni:
    print(x)
    print(prenotazioni[x])
print()
print
while True:
    for x in prenotazioni:
        print(x)
        print(prenotazioni[x])
        scelta=int(input("Premi 1 se vuoi continuare, o 2 se non vuoi "))
        if scelta == 1:
            prenotazioni_confermate.append(x)
            print()
        if scelta == 2:
            print()
        print("Elenco prenotazioni confermate")
        print(prenotazioni_confermate)
        print()
        if scelta == 1:
            print("Prossimo partecipante: ")
    print()
    print(prenotazioni_confermate)
    scelta2=int(input("Premi 1 se vuoi rivedere l'eleco dei partecipantie, o 2 se non vuoi "))
    if scelta2==1:
        print()
    else:
        break