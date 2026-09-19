contador = 1
soma = 0

while contador <= 5:
    try:  
        numeroInput = int(input(f"Digite o numero {contador} a ser somado "))
        soma += numeroInput
        contador += 1

    except Exception as ex:
        print("O valor digitado nao é um numero valido")
        print(ex)

print(f"a soma total é {soma}")