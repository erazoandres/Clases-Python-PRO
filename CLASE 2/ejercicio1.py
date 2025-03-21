import random

signos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Ingresa la longitud de tu contraseña: "))

password = ""

for i in range(longitud):
    password = password + random.choice(signos)

print("Tu contraseña es:" ,password)
