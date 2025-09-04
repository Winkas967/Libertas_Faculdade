numero = 99
contador = 0

while numero < 200:
    numero = numero + 1
    if numero % 2 == 0:
        contador = contador + 1
    print(numero)
print("*--------------------------------------*")
print(f"Tem {contador} números!")




x = 100
for x in range(2 , 200, 2):
    print(x)