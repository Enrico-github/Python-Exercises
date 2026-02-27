import socket 
import threading 
lock = threading.Lock()

veicoli = {
    "Fiat Idea": {"costo": 40, "disponibili": 3},
    "BMW 320 G20": {"costo": 80, "disponibili": 2},
    "Mercedez CLA220": {"costo": 100, "disponibili": 1}
}

def gestione_client(conn, addr):
    print(f"connessione con {addr}")

    lista_auto = ",".join(veicoli.keys())
    conn.sendall(lista_auto.encode())

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            modello, giorni = data.split(",")
            
            try:
                giorni = int(giorni)
                if giorni <= 0:
                    risposta = "numero di giorni non vaido"
                else:
                    with lock:
                        if modello not in veicoli:
                            risposta = "veicolo non trovato"
                        elif veicoli[modello]["disponibili"] <= 0:
                            risposta = "veicolo non disponibile"
                        else:
                            costo_giornaliero = veicoli[modello]["costo"] 
                            totale = costo_giornaliero * giorni
                            sconto = 0
                            
                            if giorni >= 7:
                                sconmto = totale * 0.15
                                finale = totale - sconto
                                
                                risposta = (
                                    f"modello: {modello}\n"
                                    f"giorni: {giorni}\n"
                                    f"costo giornaliero: {costo_giornaliero}€\n"
                                    f"totale: {totale}€\n"
                                    f"sconto: {sconto}€\n"
                                    f"da pagare: {finale}€\n" 
                                )
                                veicoli[modello]["disponibili"] -= 1
            except:
                risposta = "inserimento errato"
                    
            conn.sendall(risposta.encode())
                     
        except:
            break
                
    print(f"connessione chiusa con {addr}")
    conn.close()
                
def start_server():
    server_socket = socket.socket(socket.AF.INET,socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    
    print("server noleggio auto in ascolto...")
    
    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(
            target = gestione_client,
            args = (conn, addr)
        )
        client_thread.start()
        
        
        if __name__ == "__main__":
            start_server()
