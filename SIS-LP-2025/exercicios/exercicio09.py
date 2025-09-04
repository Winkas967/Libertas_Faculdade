import random

number = int(input("Digite um número: "))
soma = 0

for x in range(number):
    i = random.randint(1,10)
    print(i)
    soma = soma + i
    
print(f"A soma dos números são: {soma}")
