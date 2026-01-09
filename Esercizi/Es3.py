def valore_totale_magazzino(prodotti):
    totale = 0
    for p in prodotti:
        totale += p["prezzo"] * p["quantità"]
    return totale

prodotti = []

n = int(input("Quanti prodotti? "))

for i in range(n):
    nome = input("Nome prodotto: ")
    prezzo = float(input("Prezzo: "))
    quantita = int(input("Quantità: "))
    prodotti.append({"nome": nome, "prezzo": prezzo, "quantità": quantita})

# Prodotto con valore più alto
max_prodotto = prodotti[0]

for p in prodotti:
    if p["prezzo"] * p["quantità"] > max_prodotto["prezzo"] * max_prodotto["quantità"]:
        max_prodotto = p

# Prodotti esauriti
esauriti = []

for p in prodotti:
    if p["quantità"] == 0:
        esauriti.append(p["nome"])

print("\n--- RIEPILOGO MAGAZZINO ---")
for p in prodotti:
    valore = p["prezzo"] * p["quantità"]
    print(p["nome"], "- Valore:", valore)

print("\nValore totale magazzino:", valore_totale_magazzino(prodotti))
print("Prodotto più prezioso:", max_prodotto["nome"])
print("Prodotti esauriti:", esauriti)
