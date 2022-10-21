count = 0
total = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        print("Count:", count, "Total:", total, "Average:", round(total / count, 2))
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = float(total) + float(num)
