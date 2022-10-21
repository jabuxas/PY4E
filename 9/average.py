jabuxa = list()
while True:
    inp = input("Enter value: ")
    if inp == "done":
        break
    inp = float(inp)
    jabuxa.append(inp)
print("Average is:", sum(jabuxa) / len(jabuxa))
