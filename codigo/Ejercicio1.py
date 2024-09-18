import random

while True:
    r = random.randint(1,100)
    n = 0
    contador = 1
    while r != n:
        print("Intento {}".format(contador))
        while True:
            n = int(input("Adivine el numero, Ingrese un numero del 1 al 100: "))
            if n >= 1 and n <= 100:
                break
            else:
                print("Por favor introduce un número valido")
        if n < r:
            print("Demasiado bajo, Intenta denuevo")
        elif n > r:
            print("Demasiado alto, Intenta denuevo")
        elif n == r:
            print("Felicidades acertaste en {} Intentos".format(contador))
            break
        contador += 1
    opcion = input("Si quiere jugar otra vez aprete cualquier tecla, sino aprete x minuscula: ")
    if opcion == "x":
        break
