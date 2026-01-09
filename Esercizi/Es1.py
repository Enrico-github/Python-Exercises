def media(voti):
    return sum(voti) / len(voti)

studenti = []

n = int(input("Quanti studenti ci sono? "))

for i in range(n):
    nome = input("Nome studente: ")
    voti_str = input("Inserisci i voti separati da spazio: ")
    voti = list(map(int, voti_str.split()))
    studenti.append({"nome": nome, "voti": voti})

# Calcolo medie
studente_max = studenti[0]
studente_min = studenti[0]

promossi = []

for s in studenti:
    m = media(s["voti"])
    s["media"] = m

    if m > studente_max["media"]:
        studente_max = s
    if m < studente_min["media"]:
        studente_min = s

    if m >= 6:
        promossi.append(s["nome"])

# Riepilogo
print("\n--- RIEPILOGO ---")
for s in studenti:
    stato = "Promosso" if s["media"] >= 6 else "Bocciato"
    print(s["nome"], "- Media:", round(s["media"], 2), "-", stato)

print("\nMedia più alta:", studente_max["nome"])
print("Media più bassa:", studente_min["nome"])
print("Studenti promossi:", promossi)
