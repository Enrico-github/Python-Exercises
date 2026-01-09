def conta_parole(parole):
    diz = {}
    for p in parole:
        if p in diz:
            diz[p] += 1
        else:
            diz[p] = 1
    return diz

frase = input("Inserisci una frase: ").lower()
parole = frase.split()

conteggio = conta_parole(parole)

piu_lunga = parole[0]
piu_corta = parole[0]

for p in parole:
    if len(p) > len(piu_lunga):
        piu_lunga = p
    if len(p) < len(piu_corta):
        piu_corta = p

ripetute = []

for p in conteggio:
    if conteggio[p] > 1:
        ripetute.append(p)

print("\nLista parole:", parole)
print("Conteggio parole:", conteggio)
print("Parola più lunga:", piu_lunga)
print("Parola più corta:", piu_corta)
print("Parole ripetute:", ripetute)
