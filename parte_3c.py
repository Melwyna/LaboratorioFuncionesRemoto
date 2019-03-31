def is_prime(b):
    pepe = 0

    for i in range(1, b + 1):
        if b % i == 0:
            pepe += 1

    if pepe == 2:
        return 1

    else:
        return 0


contprimo = 0
cont_primo = 0
while True:

    try:

        x = int(input("Ingrese un numero"))

        cd = is_prime(x)
        if cd == 1:
            contprimo += 1
            cont_primo += 1

        cdp = is_prime(cont_primo)
        if cdp == 1:
            x1 = ("el numero de veces es primo")
        if cdp == 0:
            x1 = ("el numero de veces no es primo")
        if x <= 0:
            print("-1")
            print("No se puede determinar y se calcularon:", contprimo, "primos y", x1)
            break

        print(cd)

    except ValueError:
        print("-1")
        print("No se permite ingresar letras y se calcularon:", contprimo, "primos y", x1)
