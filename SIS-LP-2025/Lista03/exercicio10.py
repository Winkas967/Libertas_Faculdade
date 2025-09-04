senha = input("Digite seu senha: ")

tent = 0
acesso = False

while tent < 3:
    tentativas = input("Digite seu senha novamente: ")  
    if tentativas == senha:
        acesso = True
        print("Acesso Liberado!")
        break
    else:
        print("Senha incorreta!")
    tent +=1
    
if not acesso:
    print("Acesso negado!!")