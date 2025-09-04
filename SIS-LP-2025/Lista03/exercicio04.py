import random

print("Tente adivinhar o número entre 1 e 100. Você tem 10 tentativas.")

num = random.randint (1, 100)

stop = 0

while stop < 10:
    
    resposta = int(input(f"Tentativa {stop + 1}: "))
    
    stop = stop + 1
    
    if resposta > num:
        print("Mais baixo!")
    elif resposta < num:
        print("Mais alto!")
    else:
        print(f"Parabéns! Você acertou o número {num} em {stop} tentativas!")
        if stop < 5:
            print("Bônus! Você acertou em menos de 5 tentativas! Muito bem!")
        break
    
else:
    print(f"Você perdeu! O número era {num}.")