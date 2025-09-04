palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palavra1 = palavra1.upper()
palavra2 = palavra2.upper()
palavra1 = sorted(palavra1)
palavra2 = sorted(palavra2)
if palavra1 == palavra2:
    print("São anagramas!")
else:
    print("Não são anagramas!")
