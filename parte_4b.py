def is_prime(a):
    cont = 0
    con_1 = 0
    for i in range(1, a):
        if a % i == 0:
            cont += 1
            con_1 = i + con_1
            x1 = con_1
        a1 = a - x1
    if -3 <= a1 <= 3:
        print("el", a, "es un numero casi perfecto")
    else:
        print("No es un número casi perfecto")


a = int(input("Ingrese un numero:"))
is_prime(a)
