while True:
    num = int(input("Digite um número inteiro positivo: "))

    divisores = []

    for i in range(2, num):
        if num % i == 0:
            divisores.append(i)
    if not divisores:
        print(f"{num} é um número primo.")
    else:
        print(f"Divisores de {num} (excluindo 1 e ele mesmo): {divisores}")
    continuar = input("Deseja analisar outro número? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa encerrado.")
        break