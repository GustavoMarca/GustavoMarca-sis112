lista = [1,2,3,4,5]
print(lista)
print(lista[2])
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matriz[1][2])

lista2 = ["a","b","c","d"]
print(type(lista2[3]))

listastring =["a",2.2,"c",10,["z","x","9"]]
print(type(listastring[4][2]))

estudiantes = []
notas = []
estudian = int(input("Ingrese la cantidad de estudiantes: "))
for i in range (estudian):
    num = int(input("Ingrese cuantas notas ingresara del estudiante {}".format(i+1)))
    print("Estudiante {}".format(i+1))
    for q in range(num):
        nota = int(input("Ingrese su nota {}: ".format(q+1)))
        notas.append(nota)
    estudiantes.append(notas)
    notas = []
print(estudiantes)