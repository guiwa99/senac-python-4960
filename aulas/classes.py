from usuario import Usuario

print("Execução normal do arquivo...")        
usuario = Usuario("Guilherme", 27)
usuario2 = Usuario("Douglas", 32)

print(f"objeto usuario {usuario}")
print(f"objeto usuario2 {usuario2}")

print(usuario.nome)
print(usuario.idade)

usuario.idade = 28

print(f"nova idade {usuario.idade}")
usuario.apresentar()
usuario2.apresentar()