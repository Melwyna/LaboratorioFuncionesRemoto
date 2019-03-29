def a_power_b():
    produc = 1

    for i in range(0, b):
        produc = produc * a

    print(produc)


a = int(input("Escribe el primer numero: "))
b = int(input("Escribe el segundo numero: "))

a_power_b()
