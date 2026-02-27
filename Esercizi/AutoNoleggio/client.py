import socket
import tkinter as tk
from tkinter import messagebox

def connetti_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost',12345))
    return client

def ricevi_auto(client):
    data = client.recv(1024).decode()
    lista = data.split(",")
    return lista

def noleggia():
    auto = auto_var.get()
    giorni =entry_giorni.get()
    
    if giorni == "":
        messagebox.showerror("errore")
        return
    if not giorni.isdigit():
        messagebox.showerror("errore")
        return
    giorni = int(giorni)
    
    if giorni <= 0:
        messagebox.showerror("errore")
        return
    
    messaggio = auto + ","+ str(giorni)
    client.sendall(messaggio.encode())
    
    risposta = client.recv(1024).decode()
    
    messagebox.showerror("riepilogo", risposta)
    
    entry_giorni.delete(0, tk.END)
    
    client = connetti_server()
    lista_auto = ricevi_auto(client)
    
    root = tk.Tk()
    root.title("noleggio auto")
    
    auto_var = tk.StringVar(root)
    auto_var.set(lista_auto[0])
    
    tk.label(root, text="inserisci giorni di noleggio").pack(pady=5)
    entry_giorni = tk.Entry(root)
    entry_giorni.pack(pady=5)
    
    tk.Button(root,  text="noleggia", command=noleggia).pack(pady=10)
    
    root.mainloop()
    client.close()
