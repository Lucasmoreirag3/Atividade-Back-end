notas = []
while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media}")
else:
    print("Nenhuma nota foi digitada.")