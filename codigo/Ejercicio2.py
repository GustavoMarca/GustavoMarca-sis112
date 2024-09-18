import random

lista= [["G","A","T","O"],["C","A","S","A"],["P","R","O","G","R","A","M","A","C","I","O","N"],["B","I","O","M","E","D","I","C","A"],["T","A","R","E","A"],["E","J","E","R","C","I","C","I","O"]]

while True:
    a = []
    palabra = random.choice(lista)
    rango = len(palabra) 
    for i in range (rango):
        a.append("_")
    print("Ahorcados")
    Intentos = 5
    usados = [] 
    while Intentos > 0:
        while True:
            print("Tienes {} intentos".format(Intentos))
            print("Palabra: ", " ".join(a))
            print("Letras usadas: ", " ".join(usados))
            letra = input("Ingrese una letra para adivinar: ").upper()
            if letra in usados:
                print("Ya has usado esa letra, intenta con otra.")
                continue
            else:
                break
        usados.append(letra)
        acertado = 0
        for i in range(len(palabra)):
            if letra == palabra[i]:
                a[i] = palabra[i]
                acertado += 1
        if acertado == 0:
            Intentos -= 1
        if "_" not in a:
            print("Adivinaste la palabra:", "".join(palabra))
            break
    if Intentos == 0:
        print("perdiste, la palabra era:", "".join(palabra))
    opcion = input("Para cerrar presiona X, para jugar denuevo cualuier letra: ")
    if opcion.upper == "X":
        break
