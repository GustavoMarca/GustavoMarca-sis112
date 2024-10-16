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


lista = [1.1, 2.3, 4.5, 5.7, 6.9]
numero = 4.5
resultado = busqueda_binaria(lista, numero) 
print(resultado)


