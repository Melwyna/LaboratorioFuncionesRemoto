def is_prime():
    cont = 0
    for i in range(1, b + 1):
        if b % i == 0:
            cont += 1

    if cont == 2:
        print("is a prime number")
    else:
        print("is not a prime number")


b = int(input("Ingrese un numero"))
is_prime()
