def is_prime(b):
    pepe = 0
    for i in range(1, b + 1):
        if b % i == 0:
            pepe += 1

    if pepe == 2:
        return 1
    else:
        return 0


while True:

    try:

        x = int(input("Ingrese un numero:"))
        if x <= 0:
            print("-1")
            print("No se puede determinar")
            break

        cd = is_prime(x)
        print(cd)

    except ValueError:
        print("-1")
        print("No se permite ingresar letras")

