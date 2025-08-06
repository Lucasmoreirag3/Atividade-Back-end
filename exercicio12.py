import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Advinhe o número (entre 1 e 100): "))
    if palpite < numero_secreto:
        print("Maior!")
    elif palpite > numero_secreto:
        print("Menor!")
    else:
        print("Parabéns! Você acertou!")
        break