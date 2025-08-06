positivos = 0
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero > 0:
        positivos += 1
print(f"Você digitou {positivos} números positivos.")