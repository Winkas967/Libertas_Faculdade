import math

n = int(input("Digite o primeiro número: "))
k = int(input("Digite o segundo número: "))

if n == k:
        print("A resposta é 1")
elif k == 0:
        print("A resposta é 1")
elif k == 1:
        print(f"A resposta é igual a {n}")
elif n == 0:
        print("Não existe")
else:
    if k > n - k:
        k = n - k
    resposta = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    print(f"A resposta é {resposta}")
    