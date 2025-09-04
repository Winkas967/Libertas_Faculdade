ingredientes = ["tomate", "agrião", "filé de frango", "pão de queijo", "mel"]
total = 0

for i in ingredientes:
    for j in ingredientes:
        for k in ingredientes:
            print(i, ",", j, ",", k)
            total += 1

print("\nQuantidade total de combinações:", total)