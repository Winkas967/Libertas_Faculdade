lista = [input(str(""Preencha essa lista com 10 números de sua escolha: ")]
cont = []

for i in lista:
    for n in lista:
        for x in cont:
            if i != n:
                cont.append(x)
                print(cont)
            else:
                print("bolAS")
