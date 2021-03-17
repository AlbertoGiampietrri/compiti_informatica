# un'azienda vende prodotti in tutta Italia e la rete di vendita è suddivisa in quattro zone:Nord, Centro, Sud e Isole.
# dopo aver acquisito in un array il fatturato nelle quattro zone, calcola: il totale fatturato, i valori in percentuale delle vendite nelle quattro zone rispetto al totale
lista=[]
fatturato_nord=float(input("Quanto corrisponde il fatturato della zona Nord?"))
lista.append(fatturato_nord)
fatturato_centro=float(input("Quanto corrisponde il fatturato della zona Centro?"))
lista.append(fatturato_centro)
fatturato_sud=float(input("Quanto corrisponde il fatturato della zona Sud?"))
lista.append(fatturato_sud)
fatturato_isole=float(input("Quantocor corrisponde il fatturato delle isole?"))
lista.append(fatturato_isole)
totale=sum(lista) 
print("Il fatturato totale è", totale)
print("Il valore in percentuale rispetto al totale del Nord è", fatturato_nord*100/totale)
print("Il valore in percentuale rispetto al totale del Centro è", fattura_centro*100/totale)
print("Il valore in percentuale rispetto al totale del Sud è", fatturato_sud*100/totale)
print("il valore in percentuale rispetto al totale delle Isole è", fatturato_isole*100/totale)