inv = float(input("Qual o valor do investimento desse mês? R$: "))
juros = float(input("Qual o valor dos juros? %: ")) / 100

saldo = 0.0
ano = 1

continuar = "s"

while continuar == "s":
    mes = 1
    while mes <= 12:
        saldo = saldo + saldo * juros
        saldo = saldo + inv
        mes += 1
        
    print(f"Após {ano} ano(s), o saldo total do investimento é de: R${saldo}")
    continuar = input("Deseja calcular o próximo ano? (s/n): ")
    
print("Simulação encerrada, obrigado!")