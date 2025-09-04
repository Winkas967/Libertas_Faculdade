# Exercicio A
a = int(input ("valor: "))
b = int(input ("valor: "))
c = int(input ("valor: "))
r = a + b + c 
print (r) 

# Exercicio .
prova1= int(input ("Nota da prova1: ")) 
prova2 = int(input ("Nota da prova2: ")) 
prova_total = prova1 * 3 + prova2 * 3
trabalho = int(input ("Nota do trabalho: "))
participacao = int(input ("Nota de participação: "))
 
r = (prova_total + 3*trabalho + participacao) / 10
print(r)

#Exercicio C+

x = input("Você é homem ou mulher? ")
altura = float(input("Qual é sua altura? "))

if x == "Mulher":
    mulher = float((62.1 * altura) - 44.7)
    print(f"Seu peso ideal é: {mulher} KG ")
    
if x == "Homem":
    homem = float((72.7 * altura) - 58)
    print(f"Seu peso ideal é: {homem} KG ")