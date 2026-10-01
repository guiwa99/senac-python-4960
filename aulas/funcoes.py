# def saudacao():
#     print("Olá, mundo")

# saudacao()

# def saudacao_com_nome(nome="Aluno"):
#     print(f"Olá, meu nome é {nome}")

# saudacao_com_nome("Guilherme")
# saudacao_com_nome("Douglas")
# saudacao_com_nome()

# def somar(a, b):
#     soma = a + b
#     return soma

# print(somar(5, 2))

def cadastrar_usuario(nome: str, idade: int = 18):
    print(f"Cadastrando nome {nome} {type(nome)}")
    print(f"Cadastrando idade {idade} {type(idade)}")

cadastrar_usuario("Guilherme", 27)
cadastrar_usuario("João")

cadastrar_usuario(nome="Douglas", idade=32)
cadastrar_usuario(idade=40, nome="Eloi")
# cadastrar_usuario(idade=40, "Marlene") dá erro
cadastrar_usuario("Marlene", idade=40)
cadastrar_usuario(10, "texto")