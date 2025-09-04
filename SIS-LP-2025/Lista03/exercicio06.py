print("=== Números Perfeitos ===")
num = int(input("Quantos números perfeitos você deseja ver? "))

quantidade_encontrada = 0
numero = 2

while quantidade_encontrada < num:
    soma_divisores = 0
    divisor = 1

    while divisor < numero:
        if numero % divisor == 0:
            soma_divisores += divisor
        divisor += 1

    if soma_divisores == numero:
        print(numero)
        quantidade_encontrada += 1

    numero += 1
