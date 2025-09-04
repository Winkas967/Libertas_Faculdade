print("Testando a fórmula: (P ^ Q) <-> ¬(R v S)")

totallinhas = 0
possibilidades = [True,False]

for P in possibilidades:
    for Q in possibilidades:
        for R in possibilidades:
            for S in possibilidades:
        
                if (P and Q) == (not(R and S)):
                    resultadoformula = True
                else:
                    resultadoformula = False
                print(f"P = {P} \t Q = {Q} \t R = {R} \t S={S} \t formula = {resultadoformula}")
                totallinhas+=1
print(f"Total de linhas: {totallinhas}")