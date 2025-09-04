"""notas = []
notas.append (9)
print(notas)
print(len(notas))

notas.append(55)
print(notas)
print(len(notas))

notas.append (350)
print(notas)
print(len(notas))

soma = sum(notas)
print(f"a soma = {soma}")

for indice in range(len(notas)):
    valor = notas[indice]
    print(f"{indice} -> conteudo {valor}")"""
    
    
nomes = []
notas = []

qtd = int(input("Digite a quantidade de alunos a serem registrados: "))

print("---lançar notas---")
for indice in range(qtd):
    nom = input("digite nome: ")
    valor = float(input("digite nota: "))
    nomes.append(nom)
    notas.append(valor)

media = sum(notas)/len(notas)
print("----------")
print(f"media: {media}")
print("----------")
for indice in range(len(notas)):
    print(f"{indice} - {nomes[indice]} - {notas[indice]}")
    if notas[indice] > media:
        print(f"Parabens {nomes[indice]} !!! ")