# Declaração de Conjuntos
print("Declaração de Conjuntos:")

S = {1, 2, 3}          # conjunto criado com chaves
R = set([2, 5, 9, 1])  # conjunto criado a partir de lista

print("O conjunto S possui os seguintes elementos:", S)
print("O conjunto R possui os seguintes elementos:", R)

# Percorrer elementos do conjunto
print("")
print("Percorrendo os elementos do conjunto S:")
for x in S:
    print(x)

print("")
print("Percorrendo os elementos do conjunto R:")
for x in R:
    print(x)

# Verificar existência de elementos no conjunto
print("")
print("Verificando a existência de elementos em um conjunto:")

# Verifica se 1 está nos conjuntos
print("O número 1 está em S?", 1 in S)
print("O número 1 está em R?", 1 in R)

# Verifica se 8 está nos conjuntos
print("O número 8 está em S?", 8 in S)
print("O número 8 está em R?", 8 in R)

# Adicionar elementos a um conjunto
print("")
print("Adicionando um elemento a um conjunto:")

print("Conjunto S antes de adicionar:", S)
print("Conjunto R antes de adicionar:", R)

# Adicionando elementos
S.add(4)  # adiciona o número 4 ao conjunto S
R.add(6)  # adiciona o número 6 ao conjunto R

print("Conjunto S depois de adicionar:", S)
print("Conjunto R depois de adicionar:", R)

# Adicionar vários elementos a um conjunto
print("")
print("Adicionando vários elementos a um conjunto:")

print("Conjunto S antes do update:", S)
print("Conjunto R antes do update:", R)

# Adicionando vários elementos de uma vez
S.update({7, 8, 10, 15, 99})  # adiciona vários elementos ao conjunto S
R.update({5, 6, 7})           # adiciona vários elementos ao conjunto R

print("Conjunto S depois do update:", S)
print("Conjunto R depois do update:", R)

# Cardinalidade: contando o número de elementos em um conjunto
print("")
print("Contando o número de elementos em um conjunto:")

print("Conjunto S:", S)
print("Número de elementos em S:", len(S))

print("Conjunto R:", R)
print("Número de elementos em R:", len(R))

# Removendo elementos de um conjunto
print("")
print("Removendo elementos de um conjunto:")

print("Conjunto S antes da remoção:", S)
print("Conjunto R antes da remoção:", R)

# Removendo elementos
S.remove(99)   # remove o elemento 99 do conjunto S; gera erro se não existir
R.discard(9)   # remove o elemento 9 do conjunto R; não gera erro se não  existir

print("Conjunto S depois da remoção:", S)
print("Conjunto R depois da remoção:", R)

# Remover um elemento arbitrário de um conjunto
print("")
print("Removendo um elemento de um conjunto com pop():")

print("Conjunto S antes do pop():", S)
print("Conjunto R antes do pop():", R)

# Remove um elemento arbitrário
S.pop()
R.pop()

print("Conjunto S após pop():", S)
print("Conjunto R após pop():", R)

# Limpar (esvaziar) os conjuntos
print("")
print("Esvaziando os conjuntos:")

print("Conjunto S antes do clear():", S)
print("Conjunto R antes do clear():", R)

# Esvaziando os conjuntos
S.clear()
R.clear()

print("Conjunto S após clear():", S)
print("Conjunto R após clear():", R)

# Excluindo conjuntos completamente
print("")
print("Excluindo os conjuntos S e R com del:")

# Criando os conjuntos novamente para o exemplo
S = {1, 2, 3}
R = {2, 5, 9, 1}

print("Conjunto S:", S)
print("Conjunto R:", R)

# Excluindo os conjuntos
del S
del R

# Tentando imprimir os conjuntos após del vai gerar erro
# print(S)  # NameError: name 'S' is not defined
# print(R)  # NameError: name 'R' is not defined

# Criando os conjuntos novamente
S = {1, 2, 3, 4}
R = {2, 5, 9, 1}

print("Conjunto S original:", S)
print("Conjunto R original:", R)

# Gerando cópias dos conjuntos
S_copy = S.copy()
R_copy = R.copy()

print("Cópia de S:", S_copy)
print("Cópia de R:", R_copy)

# Modificando as cópias
S_copy.add(99)
R_copy.remove(1)

print("S após modificar a cópia:", S)
print("S_copy após adicionar 99:", S_copy)

print("R após modificar a cópia:", R)
print("R_copy após remover 1:", R_copy)