import funcion

while True:
    opcion = funcion.opciones()
    if opcion == 1:
        X = int(input("""Si quieres de metros a km apreta 1
        Si quieres de km a metros apreta 2
        :"""))
        if X == 1:
            m = int(input("Ingresa cuantos metros convertir: "))
            print("Tienes {} km".format(funcion.metros_km(m))) 
        elif X == 2:
            km = int(input("Ingresa cuantos km convertir: "))
            print("Tines {} metros".format(funcion.km_metros(km)))
    elif opcion == 2:
        X = int(input("""Si quieres de g a kg apreta 1
        Si quieres de kg a g apreta 2 
        :"""))
        if X ==  1:
            g = int(input("Ingrese cuantos g convertir: "))
            print("Tienes {} kg".format(funcion.g_kg(g)))
        elif X== 2:
            kg = int(input("Ingrese cuantos kg convertir: "))
            print("Tienes {} g".format(funcion.kg_g(kg)))
    elif opcion == 3:
        X = int(input("""Si quieres de centigrado a farenheit
        Si quieres de farenheit a centrigrado
        :"""))
        if X == 1:
            c = int(input("Ingrese cuantos centigrados convertir: "))
            print("Tienes {} k°".format(funcion.c_f(c)))
        elif X == 2:
            f = int(input("Ingrese cuantos ferenheit convertir: "))
            print("Tienes {} C°".format(funcion.f_c(f)))
    elif opcion == 4:
        break
        