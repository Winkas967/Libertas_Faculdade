temp = float(input("Digite a temperatura em Cº: "))

if temp < 10:
    print("Muito frio!!!")
elif 10 <= temp <= 25:
    print("Clima agradável!")
else:
    print("Calor!!!")
