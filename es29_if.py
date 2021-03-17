print()
d={23:15000,27:28000,38:55000,41:75000,43:1000000}
reddito=int(input("Inserisci il reddito "))
if reddito<=d[23]:
    imposta=reddito*23/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)
if reddito<=d[27] and reddito>=d[23]:
    imposta=3450+reddito*27/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)
if reddito<=d[38] and reddito>=d[27]:
    imposta=3450+3510+reddito*38/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)  
if reddito<=d[41] and reddito>=d[38]:
    imposta=3450+3510+10260+reddito*41/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)
if reddito<=d[43] and reddito>=d[41]:
    imposta=3450+3510+10260+8200+reddito*23/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)
print()