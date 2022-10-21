jader = list()
while True:
    question = input("Adicionar items a lista: ")
    if question == "Stop":
        break
    jader.append(question)
    jader.sort()

print(max(jader), min(jader))
