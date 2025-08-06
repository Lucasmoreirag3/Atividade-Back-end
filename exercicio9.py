senha_correta = "2345"
while True:
    senha = input ("Diste a sua senha:")
    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente Novamente.")
        