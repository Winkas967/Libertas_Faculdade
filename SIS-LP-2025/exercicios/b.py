soma = 0
num = int(input("Digite números (Digite 0 para parar): "))
while num != 0:
    soma+=num
    num = int(input("Digite números (Digite 0 para parar): "))
print(f"Soma total: {soma}")