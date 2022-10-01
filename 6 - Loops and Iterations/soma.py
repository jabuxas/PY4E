def calc():
    first = input("Qual é o primeiro número? ")
    second = input("Qual é o segundo número? ")
    sum = float(first) + float(second)
    print("A soma dos dois é:", round(sum, 3))

calc()
def question():
    ans = input("Quer fazer outra soma? ")
    if ans == 'Sim':
        calc()
        question()
    if ans == 'Não':
        print('Tchau')

question()
