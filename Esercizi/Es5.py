def saldo_finale(operazioni):
    return sum(operazioni)

operazioni = list(map(int, input("Inserisci operazioni: ").split()))

saldo = 0
saldo_max = 0
saldo_min = 0
saldi = []

depositi = 0
prelievi = 0

for op in operazioni:
    saldo += op
    saldi.append(saldo)

    if saldo > saldo_max:
        saldo_max = saldo
    if saldo < saldo_min:
        saldo_min = saldo

    if op > 0:
        depositi += 1
    elif op < 0:
        prelievi += 1

print("\n--- RIEPILOGO CONTO ---")
print("Saldo finale:", saldo_finale(operazioni))
print("Saldo massimo:", saldo_max)
print("Saldo minimo:", saldo_min)
print("Numero depositi:", depositi)
print("Numero prelievi:", prelievi)
print("Saldi nel tempo:", saldi)
