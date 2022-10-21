lst = list()
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    lst.append(num)

print("Maximum is", max(lst))
print("Minimum is", min(lst))
