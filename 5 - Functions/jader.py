# Define função que transforma uma letra dada em um número
def nota(letra):
    if letra == 'A':
        letra = 4
        return letra
    elif letra == 'B':
        letra = 3
        return letra
    elif letra == 'C':
        letra = 2
        return letra
    else:
        letra = 1
        return letra

# Pede input usuário para argumentos para ser usados na função

letra1 = input("Primeira nota: ")
letra2 = input("Segunda nota: ")
letra3 = input("Terceira nota: ")
letra4 = input("Quarta nota: ")

# Transforma o output da função em uma variável

primeiro = nota(letra1)
segundo = nota(letra2)
terceiro = nota(letra3)
quarto = nota(letra4)

# Média aritmética
soma = (primeiro + segundo + terceiro + quarto) / 4

# Transforma valor em boolean True ou False
if soma >= 2:
    soma = True
else:
    soma = False

# Por fim, devolve o resultado:
print(soma)
