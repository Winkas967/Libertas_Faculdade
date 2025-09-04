num = int(input("Informe um número para calcular a série de Fibonacci: "))

f0 = 0
f1 = 1

fibonacci = []

for x in range(num + 1):
    if x == 0:
        fibonacci.append(f0)
    elif x == 1:
        fibonacci.append(f1)
    else:
        fn = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(fn)
        
print("Série de Fibonacci:")
print(", ".join(str(num) for num in fibonacci))