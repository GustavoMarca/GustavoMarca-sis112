EJERCICIO1
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

EJERCICIO2
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(float(a/b))

EJERCICIO3
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print (i*i)

EJERCICIO4
def is_leap(year):
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))

EJERCICIO5 
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(i+1, end= "")


Otro problema:
n = int(input())
for i in range (n):
    if (i+1) % 2 != 0:
        print((i+1)**2)


n = int(input())
num = (n*(n+1))/2
print (num)

cantidad = int(input("Ingrese cuantas notas pondra: "))
suma = 0
for i in range (cantidad):
    nota = int(input("Ingrese la nota {}: ".format(i+1)))
    suma += (nota)
promedio= suma/cantidad
print("Promedio: {}".format(promedio))  