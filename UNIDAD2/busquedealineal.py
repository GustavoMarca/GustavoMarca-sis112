import random

def crear(mx,mn,rango):
    l = []
    for i in range(rango) :
        x = random.randint(mn, mx)
        l.append(x)
    return l

def ver(lista):


rango = int(input("Ingrese cuantos numeros quiere que tenga la lista: "))
mn = int(input("Ingrese el minimo numero de su lista: "))
mx = int(input("Ingrese el maximo numero de su lista: "))
lista = crear(mx,mn,rango)
print(lista)

