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
    n1 = int(input("Elija su numero 1: "))
    n2 = int(input("Elija su numero 2: "))
    if opcion == 1:
        total = n1+n2
    elif opcion == 2:
        total = n1-n2
    elif opcion == 3:
        total = n1*n2
    elif opcion == 4:
        total = n1/n2
    print ("El resultado es : {}".format(total))
