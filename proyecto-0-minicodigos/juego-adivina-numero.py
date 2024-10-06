import random
import os

def borrarConsola():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def jugar():

    borrarConsola()

    num_1 = random.randint(10,89)
    num_2 = num_1 + 10
    num_adivinar = random.randint(num_1, num_2)

    input("¡¡¡ADIVINA EL NÚMERO!!! Pulsa ENTER para comenzar")
    borrarConsola()

    vidas = 5
    while vidas > 0:

        num_introducido = int(input(f"\nINTRODUCE UN NÚMERO (SE ENCUENTRA ENTRE {num_1} y {num_2}): "))

        if num_introducido == num_adivinar:
            borrarConsola()
            print(f"¡¡¡HAS GANADO!!! El número es {num_adivinar}." )

            rejugar = input("\n¿Quieres volver a jugar? (s/n): ")
            if rejugar[0] == "s" or rejugar[0] == "S":
                jugar()
            else:
                quit()

        else:
            vidas -= 1

            if vidas <= 0:
                borrarConsola()
                print(f"¡¡¡HAS PERDIDO!!! El número era {num_adivinar}.")

                rejugar = input("\n¿Quieres volver a jugar? (s/n): ")
                if rejugar[0] == "s" or rejugar[0] == "S":
                    jugar()
                else:
                    quit()


            if num_adivinar < num_introducido:
                print(f"¡HAS FALLADO! Te quedan {vidas} intentos. El número es menor a {num_introducido}")
            
            else:
                print(f"¡HAS FALLADO! Te quedan {vidas} intentos. El número es mayor a {num_introducido}")  


            input("\nPulsa ENTER para continuar...")
            borrarConsola()

jugar()


        
        


        
        

    

