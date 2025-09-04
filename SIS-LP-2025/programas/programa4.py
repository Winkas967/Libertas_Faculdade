# Faça um algoritimo que calcule o valor a pagar em uma lanchonete, dada a quantidade de pasteis comprados e o preço de cada pastel, e a quantidade de refrigerante comprados, e o preço de cada refrigerante, determine o valor a ser pago!

# PASTEIS
quantidade_pastel = int(input("digite a quantidade de pasteis: "))
valor_pastel = int(input("digite o valor do pastel: "))
# REFRIGERANTE
quantidade_refrigerante = int(input("digite a quantidade de refrigerante: "))
valor_refrigerante = int(input("Digite o valor do refrigerante: "))
#VALOR
valor_finalpastel = quantidade_pastel * valor_pastel
valor_finalrefrigerante = quantidade_refrigerante * valor_refrigerante
valor_total = valor_finalpastel + valor_finalrefrigerante

print(f"O total fica em R$ {valor_total}")