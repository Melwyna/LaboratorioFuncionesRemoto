def is_prime(a):
    cont = 0
    con_1 = 0
    for i in range(1, a):
        if a % i == 0:
            cont += 1
            con_1 = i + con_1
            x1 = con_1
    if x1 == a:
        print("el", a, "es un numero perfecto")
    else:
        print("No es un número perfecto")


a = int(input("Ingrese un numero:"))
is_prime(a)
