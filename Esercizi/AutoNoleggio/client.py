import socket
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Connessione al server
# -----------------------------
def connetti_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    return client

# -----------------------------
# Ricezione lista auto
# -----------------------------
def ricevi_auto(client):
    data = client.recv(1024).decode()
    lista = data.split(",")
    return lista

# -----------------------------
# Funzione acquisto/noleggio
# -----------------------------
def noleggia():
    auto = auto_var.get()
    giorni = entry_giorni.get()

    # Controllo input vuoto
    if giorni == "":
        messagebox.showerror("Errore", "Inserisci il numero di giorni")
        return

    # Controllo input numerico
    if not giorni.isdigit():
        messagebox.showerror("Errore", "Inserire solo numeri validi")
        return

    giorni = int(giorni)

    # Controllo giorni validi
    if giorni <= 0:
        messagebox.showerror("Errore", "I giorni devono essere maggiori di 0")
        return

    # Invio richiesta al server
    messaggio = auto + "," + str(giorni)
    client.sendall(messaggio.encode())

    # Ricezione risposta
    risposta = client.recv(1024).decode()

    # Mostra riepilogo
    messagebox.showinfo("Riepilogo Noleggio", risposta)

    # Reset campo
    entry_giorni.delete(0, tk.END)

# -----------------------------
# Avvio client
# -----------------------------
client = connetti_server()
lista_auto = ricevi_auto(client)

# Creazione finestra
root = tk.Tk()
root.title("Noleggio Auto")

auto_var = tk.StringVar(root)
auto_var.set(lista_auto[0])

tk.Label(root, text="Seleziona Auto").pack(pady=5)
tk.OptionMenu(root, auto_var, *lista_auto).pack(pady=5)

tk.Label(root, text="Inserisci giorni di noleggio").pack(pady=5)
entry_giorni = tk.Entry(root)
entry_giorni.pack(pady=5)

tk.Button(root, text="Noleggia", command=noleggia).pack(pady=10)

root.mainloop()
client.close()
