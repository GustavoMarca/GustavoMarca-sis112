def opciones():
    print("""Elija que quiere realizar:
    1. Conversion Longitud
    2. Conversion Masa
    3. Conversion Temperatura
    4. Apagar""")
    op = int(input("Elija: "))
    return op

def metros_km(m):
    longitud = m / 1000
    return longitud

def km_metros(km):
    longitud = km * 1000
    return longitud

def g_kg(g):
    masa = g / 1000
    return masa 
def kg_g(kg):
    masa = kg * 1000

def c_f(c):
    temperatura = (c*1.8)+32
    return temperatura

def f_c(f):
    temperatura = (f-32)/1.8
    return temperatura
