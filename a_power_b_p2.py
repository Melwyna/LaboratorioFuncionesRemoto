def a_power_b(a, b):
    produc = 1

    for i in range(0, b):
        produc = produc * a

    return produc


while True:

    a = int(input("Escribe el primer numero: "))

    if a == 0:
        print("Chao")
        break

    b = int(input("Escribe el segundo numero: "))

    r = a_power_b(a, b)

    print(r)