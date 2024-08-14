def suma(a,b):
    total = a+b
    return total
def resta(a,b):
    total = a-b
    return total
def multiplicacion(a,b):
    total = a*b
    return total
def division(a,b):
    total = a/b
    return total
def Main():
    while True: 
        print("""Calculadora
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Cerrar""")
        opcion = int(input("Elija el numero de opcion: "))
        if opcion ==5:
            break
        a = int(input("Elija su numero 1: "))
        b = int(input("Elija su numero 2: "))
        if opcion == 1:
            total = suma(a,b)
        elif opcion == 2:
            total = resta(a,b)
        elif opcion == 3:
            total = multiplicacion(a,b)
        elif opcion == 4:
            total = division(a,b)
        print ("El resultado es : {}".format(total))
Main()
