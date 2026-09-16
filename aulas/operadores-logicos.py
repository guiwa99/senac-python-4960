soma = 2 + 5
multiplicacao = 2 * 6

# E
if soma > 10 and multiplicacao > 10: 
    print("a soma e a multiplicacao sao maiores que 10")
else:
    print("a soma e a multiplicacao nao sao maiores que 10")

# OU
if soma > 11 or multiplicacao > 11:
    print("a soma ou multiplicacao sao maiores que 11")
else:
    print("nem a soma nem a multiplicacao sao maiores que 11")

# NEGACAO
if not soma > 10:
    print("A soma nao é maior que 10")