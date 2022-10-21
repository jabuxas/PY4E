num = input("Quais são suas notas em matéria X? ")
num = num.split()
all = 0
for n in num:
    all = all + int(n)
print("Sua média é:", all / len(num))
