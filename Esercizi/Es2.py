def media(lista):
    return sum(lista) / len(lista)

numeri = list(map(int, input("Inserisci numeri separati da spazio: ").split()))

m = media(numeri)

sopra = 0
sotto = 0
maggiori = []

for n in numeri:
    if n > m:
        sopra += 1
        maggiori.append(n)
    elif n < m:
        sotto += 1

# Sequenza più lunga di numeri uguali consecutivi
max_seq = 1
corrente = 1

for i in range(1, len(numeri)):
    if numeri[i] == numeri[i - 1]:
        corrente += 1
        if corrente > max_seq:
            max_seq = corrente
    else:
        corrente = 1

print("\nMedia:", m)
print("Numeri sopra la media:", sopra)
print("Numeri sotto la media:", sotto)
print("Lista numeri maggiori della media:", maggiori)
print("Sequenza consecutiva più lunga:", max_seq)
