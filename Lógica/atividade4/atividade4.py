vars = ['A', 'B', 'C', 'D']

formula1 = input("Digite a fórmula 1 (use A, B, C, D como variáveis): ")
formula2 = input("Digite a fórmula 2 (use A, B, C, D como variáveis): ")

combinacoes = []
valores_possiveis = [True, False]
for a in valores_possiveis:
    for b in valores_possiveis:
        for c in valores_possiveis:
            for d in valores_possiveis:
                combinacoes.append((a, b, c, d))

resultados1 = []
for valores in combinacoes:
    A, B, C, D = valores

    resultado = False
    permitido = "ABCDandor() not TrueFalse "
    ok = True
    for char in formula1:
        if char not in permitido:
            ok = False
            break

    if ok:
        resultado = eval(formula1)

    resultados1.append(resultado)
    print(f"A={'T' if A else 'F'} B={'T' if B else 'F'} C={'T' if C else 'F'} D={'T' if D else 'F'} Fórmula={'T' if resultado else 'F'}")

total_linhas = len(combinacoes)
total_T = resultados1.count(True)
total_F = resultados1.count(False)
print(f"Total de linhas: {total_linhas}")
print(f"Total de linhas com resultado F: {total_F}")
print(f"Total de linhas com resultado T: {total_T}")

if total_T == total_linhas:
    print(f"Análise da propriedade semântica da fórmula {formula1}:")
    print("Esta fórmula é TAUTOLOGICA")
elif total_F == total_linhas:
    print(f"Análise da propriedade semântica da fórmula {formula1}:")
    print("Esta fórmula é CONTRADITORIA")
else:
    print(f"Análise da propriedade semântica da fórmula {formula1}:")
    print("Esta fórmula é SATISFATORIA")

print()

resultados2 = []
for valores in combinacoes:
    A, B, C, D = valores

    resultado = False
    permitido = "ABCDandor() not TrueFalse "
    ok = True
    for char in formula2:
        if char not in permitido:
            ok = False
            break

    if ok:
        resultado = eval(formula2)

    resultados2.append(resultado)
    print(f"A={'T' if A else 'F'} B={'T' if B else 'F'} C={'T' if C else 'F'} D={'T' if D else 'F'} Fórmula={'T' if resultado else 'F'}")

total_linhas = len(combinacoes)
total_T = resultados2.count(True)
total_F = resultados2.count(False)
print(f"Total de linhas: {total_linhas}")
print(f"Total de linhas com resultado F: {total_F}")
print(f"Total de linhas com resultado T: {total_T}")

if total_T == total_linhas:
    print(f"Análise da propriedade semântica da fórmula {formula2}:")
    print("Esta fórmula é TAUTOLOGICA")
elif total_F == total_linhas:
    print(f"Análise da propriedade semântica da fórmula {formula2}:")
    print("Esta fórmula é CONTRADITORIA")
else:
    print(f"Análise da propriedade semântica da fórmula {formula2}:")
    print("Esta fórmula é SATISFATORIA")

print()

print("FAZENDO ANÁLISE DE EQUIVALÊNCIA ENTRE AS FÓRMULAS:")
if resultados1 == resultados2:
    print("As fórmulas são equivalentes.")
else:
    print("As fórmulas não são equivalentes.")
