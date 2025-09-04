x = int(input("Digite o valor de x (dividendo): "))
y = int(input("Digite o valor de y (divisor): "))

if y == 0:
    print("Erro: divisão por zero não é permitida.")
else:
    quociente = 0
    resto = x

    while resto >= y:
        resto -= y
        quociente += 1

    print(f"Resultado da divisão: {x} dividido por {y}")
    print(f"Quociente: {quociente}")
    print(f"Resto: {resto}")
