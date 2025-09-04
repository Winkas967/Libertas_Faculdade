A ={1,2,3,4,5,6,7,8,9}
B = {7,8,9,10,11,12,13,14,15}

print("Verifique se o número 6, 9 e 10 está em ambas os Conjuntos:", 6 and 9 and 10 in A)
print("Verifique se o número 6, 9 e 10 está em ambas os Conjuntos:", 6 and 9 and 10 in B)

A.add(10)
B.add(6)

print('-' * 100)

print("Verifique se o número 6, 9 e 10 está em ambas os Conjuntos:", 6 and 9 and 10 in A)
print("Verifique se o número 6, 9 e 10 está em ambas os Conjuntos:", 6 and 9 and 10 in B)