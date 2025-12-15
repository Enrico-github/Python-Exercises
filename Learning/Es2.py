# python è un linguaggio interpretato, il codice viene eseguito riga per riga e non nella sua interezza
print("hello world")
print(5+3)
'''
linguaggio non tipizzato
int
float
str
bool
per tipizzare si fa: nome della variabile : tipo di dato = valore
'''
x = "10"
y = int(x)  #cast ad intero
print(y+4)
nome = input("come ti chiami:")     #input serve per leggere una stringa da console
eta = int(input("quanti anni hai:"))    #legge una stringa e la converte in intero
print(f"ciao {nome}, hai {eta} anni")   #formattazione
