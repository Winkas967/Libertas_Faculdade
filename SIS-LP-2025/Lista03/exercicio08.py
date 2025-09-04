a = int(input("Digite o valor de a (menor): "))
b = int(input("Digite o valor de b (maior): "))

if a >= b:
    print("Erro: 'a' deve ser menor que 'b'.")
else:
    soma = 0
    
    for i in range(a, b):
        if i % 2 != 0: 
            soma += i
    print(f"A soma dos números ímpares entre {a} e {b} é: {soma}")
