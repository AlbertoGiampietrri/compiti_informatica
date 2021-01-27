'''
Organizza con un dizionario i dati sui conti correnti bancari, con numero del conto e saldo.
Fornito poi il numero del conto, il programma visualizza il saldo oppure un messaggio,
nel caso in cui il conto non sia presente nella mappa.
'''

mappa_conto={}
while True:
    conto=input("Inserire il numero del conto bancario ")
    saldo=input("Inserire il saldo del conto bancario ")
    mappa_conto[conto]=saldo
    risposta=int(input("Inserisci 1 se vuoi continuare, o 2 se vuoi stopparti "))
    if risposta==1:
        print()
    else:
        break

print()
conto=input("Di quale conto vuoi sapre il sado? ")
if conto in mappa_conto:
    print("Il saldo del conto:", conto, "è", mappa_conto[conto])
else:
    print("Questo conto non è presente nella mappa")