import funciones
notas = []
while True:
    print("""==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir""")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        notas = funciones.agregar(notas)
    elif opcion == 2:
        notas = funciones.eliminar(notas)
    elif opcion == 3:
        notas = funciones.modificar(notas)
    elif opcion == 4:
        funciones.mostrar(notas)
    elif opcion == 5:
        funciones.calculo(notas)
    elif opcion == 6:
        funciones.maxmin(notas)
    elif opcion == 7:
        print("CERRAR")
        break
    else:
        print("invalido")  