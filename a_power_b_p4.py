def a_power_b(a, b):
    produc = 1

    for i in range(0, b):
        produc = produc * a

    return produc


par = 0
impar = 0
error = 0
while True:

    try:

        a = int(input("Escribe el primer numero: "))

        if a == 0:
            print("Chao")
            error += 1
            print("pares:", par, "impares:", impar, "errores:", error)
            break

        b = int(input("Escribe el segundo numero: "))

        r = a_power_b(a, b)
        print(r)

        if r % 2 == 0:
            par += 1

        else:
            impar += 1

    except ValueError:
        print("No se permite escribir letras")
        error += 1
        print("pares:", par, "impares:", impar, "errores:", error)
    except StopIteration:
        print("Es valor es demasiado grande")
        error += 1
        print("pares:", par, "impares:", impar, "errores:", error)
    except:
        print("Error desconocido")
        error += 1
        print("pares:", par, "impares:", impar, "errores:", error)