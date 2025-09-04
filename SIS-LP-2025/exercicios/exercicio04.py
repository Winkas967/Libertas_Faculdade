dc_mes = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

dias_mes = {1: "31", 2: "28 ou 29", 3: "31", 4: "30", 5: "31", 6: "30", 7: "31", 8: "31", 9: "30", 10: "31", 11: "30", 12: "31"}

while True:
    mes = int(input("Digite o número do mês: "))
    
    if mes >=13:
        print("Esse número não é valido")
        
    elif mes == 0:
        print("Seu mês não pode ser igual a 0")
        
    else:
        print(f"Seu mês é {dc_mes[mes]}, e tem {dias_mes[mes]} dias.")
        break
        

    

