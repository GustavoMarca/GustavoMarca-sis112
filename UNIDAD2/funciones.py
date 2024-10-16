def agregar(notas):
    print("--- AGREGAR NOTA ---")
    while True:
        n = int(input("Ingresa la nota: "))
        if n >= 0 and n <= 100:
            break
    notas.append(n)
    print("Nota agregada exitosamente.")
    return notas

def eliminar(notas):
    print("---ELIMINAR NOTA---")
    if len(notas) == 0:
        print ("No hay notas que eliminar")
        notas = []
        return notas
    else:
        while True:
            m= int(input("Ingresa el índice de la nota a eliminar (1 para la primera nota, 2 para la segunda, etc.): "))
            if m >=1 and m <= (len(notas)):
                break
            else:
                print("No existe use otra")
        print("Nota actual: {}".format(notas[m-1]))
        notas.pop(m-1)
        print("Nota eliminada con exito")
        return notas

def modificar(notas):
    print("---MODIFICAR NOTA---")
    if len(notas) == 0:
        print ("No hay notas que eliminar")
        notas = []
        return notas
    else:
        while True:
            m= int(input("Ingresa el índice de la nota a modificar (1 para la primera nota, 2 para la segunda, etc.): "))
            if m >=1 and m <= (len(notas)):
                break
            else:
                print("No existe use otra")
        print("Nota actual: {}".format(notas[m-1]))
        while True:
            nueva = int(input("Ingresa la nueva nota: "))
            if nueva >= 0 and nueva <= 100:
                break
        notas[m-1] = nueva
        print("Nota modificada exitosamente")
        return notas

def mostrar(notas):
    print("--- LISTA DE NOTAS ---")
    if len(notas) == 0:
        print("No hay notas")
    else:
        for i in range(len(notas)):
            print("Nota {}: {}".format((i+1),(notas[i])))

def calculo(notas):
    if len(notas) == 0:
        print("No hay notas para sacar promedio")
    else:
        promedio = (sum(notas))/(len(notas))
        print("--- PROMEDIO ---")
        print("El promedio de las notas es: {}".format(promedio))

def maxmin(notas):
    print("--- NOTA MÁXIMA Y MÍNIMA ---")
    if len(notas) == 0:
        print("No hay notas para sacar minimo o maximo")
    else:
        print("Nota maxima: {}".format(max(notas)))
        print("Nota minima: {}".format(min(notas)))

