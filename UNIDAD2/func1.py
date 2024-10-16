import random
def generarlista(a,s,d,f):
    while (len(f)) != a:
        aleatorio = random.randint(d,s)
        if aleatorio not in f:
            f.append(aleatorio)
    return f



def encontrarNumero(lista,numero):
    for i in range (len(lista)):
        if lista[i] == numero:
            print(f"numero encontrado en el indice {i}")
            return 1
        
def busqueda_binaria(lista,numero):
    izquierda, derecha = 0,len(lista)-1
    while izquierda<= derecha:
        medio = (izquierda+derecha)//2
        if lista[medio]== numero:
            return medio
        elif lista[medio] < numero:
            izquierda = medio+1
        else:
            derecha = medio-1
    return -1