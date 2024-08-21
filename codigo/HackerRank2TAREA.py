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

EJERCICIO5
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