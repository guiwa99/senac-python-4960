EMAIL_CADASTRADO = "admin@email.com"
SENHA_CADASTRADA = "1234"

email_input = input("Email: ")
senha_input = input("Senha: ")

if email_input == EMAIL_CADASTRADO and senha_input == SENHA_CADASTRADA:

    print("Login realizado com sucesso!")

    input("")

else:
    print("Erro ao realizar o login.")
    print("Email ou senha incorretos!")

    input("")
