n = int(input("Digite quantos termos da sequência de Fibonacci deseja ver: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b