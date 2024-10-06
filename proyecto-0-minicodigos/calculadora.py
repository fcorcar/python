num_1 = 0
num_2 = 0
opcion = 0
resultado = 0

print("""OPERACIONES
      1. Sumar
      2. Restar
      3. Multiplicar
      4. Dividir
    """)

opcion = int(input("Introduce una opción (1-4): "))

if not (opcion > 0 and opcion < 5):
    print("Opción incorrecta")
    exit()
    

num_1 = float(input("Introduce el primer número: "))
num_2 = float(input("Introduce el segundo número: "))

if opcion == 1:
    resultado = num_1 + num_2
    print(f"{num_1} + {num_2} = {resultado}")

elif opcion == 2:
    resultado = num_1 - num_2
    print(f"{num_1} - {num_2} = {resultado}")

elif opcion == 3:
    resultado = num_1 * num_2
    print(f"{num_1} * {num_2} = {resultado}")

elif opcion == 4:
    if num_2 == 0:
        print("Nos es divisible entre 0")
        exit()

    resultado = num_1 / num_2
    print(f"{num_1} / {num_2} = {resultado}")


