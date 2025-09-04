n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("Erro: o número deve ser inteiro e positivo.")
else:
    print("Sequência de Collatz:")
    while n != 1:
        print(n, end=" → ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)