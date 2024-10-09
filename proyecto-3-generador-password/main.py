##DESARROLLA UNA HERRAMINETA QUE GENERE CONTRASEÑAS SEGURAS Y ALEATORIAS BASADAS EN LONGITUD Y CARACTERES ESPECIALES
import string
import random

longitud_pass = 16 # minimo 8 maximo 16

abecedario_low = string.ascii_lowercase
abecedario_up = string.ascii_uppercase
caracteres_especiales = string.punctuation
numeros = string.digits

conjunto = []

passwd = ""

abecedario_low_check = bool(input("abc (Escribe 's' para SI o pulsa ENTER para NO): "))
abecedario_up_check = bool(input("ABC (Escribe 's' para SI o pulsa ENTER para NO): "))
caracteres_especiales_check = bool(input("/.% (Escribe 's' para SI o pulsa ENTER para NO): "))
numeros_check = bool(input("123 (Escribe 's' para SI o pulsa ENTER para NO): "))

if abecedario_low_check:
    conjunto.append(abecedario_low)

if abecedario_up_check:
    conjunto.append(abecedario_up)
    
if caracteres_especiales_check:
    conjunto.append(caracteres_especiales)
    
if numeros_check:
    conjunto.append(numeros)

print(conjunto)


for i in range(longitud_pass):
    abe_car_num_random = random.randint(0,len(conjunto)-1)
    passwd += random.choice(conjunto[abe_car_num_random])

print(passwd)


