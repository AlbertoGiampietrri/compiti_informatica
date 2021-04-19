# Scrivi una funzione che data in ingresso una lista A contenente n parole,
# restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
def conta_lunghezze_parole(lista_A):
    lista_B = []
    for e in lista_A:
        lista_B.append(len(e))
    return lista_B
lista_A = ["ciao", "mare", "pippo", "mario", "francobollo"]
conta_lunghezze_parole(lista_A)


# Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo
# (parole che si leggono uguali anche al contrario) oppure meno.
def controlla_palindromo(parola):
    parola2 = parola[::-1]
    if parola == parola2:
        print("La parola", parola, "è un palindromo")
    else:
        print("La parola", parola, "non è un palindromo")
controlla_palindromo("bob")
