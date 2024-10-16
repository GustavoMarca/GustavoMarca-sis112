import func1 as f
import time
listaComp = int(input("Ingrese la cantidad de datos para la lista: "))
maxAl = int(input("Ingrese el numero maximo para generar los numeros aleatorrios: "))
minAl = int(input("Ingrese el numero minimo para generar los numeros aleatorrios: "))
lista = []


inicio = time.time()
f.generarlista(listaComp, minAl, maxAl, lista)
fin = time.time()
print(f"tiempo trascurrido de la generacion de la lista\n {(fin-inicio)/1000} ms")

print(lista)
print(len(lista))
print(type(lista))

print(f"tiempo trascurrido de la generacion de la lista\n {(fin-inicio)/1000} ms")


numero = int(input("Ingrese el numerp a encontrar: "))
inicio2 = time.time()
print(f.encontrarNumero(lista,numero))
fin2 = time.time()
print(f"tiempo trascurrido de encontrar numero \n {(fin2-inicio2)*1000} ms")

x = sorted(lista)
print(x)
numero = int(input("Ingrese un numero a buscar dentro de esta lista: "))

inicio3 = time.time()
resultado = f.busqueda_binaria(lista,numero)
print(resultado) 
fin3 = time.time()
print(f"tiempo trascurrido de encontrar numero \n {(fin3-inicio3)*1000} ms")