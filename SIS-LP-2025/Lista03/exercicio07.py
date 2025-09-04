numero = int(input("Digite o número que deseja testar: "))

verificacao = 2
encontrado = False
stop = 0

while stop <= 5:
    resposta = verificacao * (verificacao +1) * (verificacao +2)
    
    if resposta == numero:
        encontrado = True
        break
    
    verificacao +=1
    stop +=1
    
if encontrado:
    print(f"O número {numero} pode ser escrito como produto de {verificacao}, {verificacao + 1} e {verificacao + 2}.")
else:
    print(f"O número {numero} NÃO pode ser escrito como produto de 3 números inteiros consecutivos entre 2 e 9.")
