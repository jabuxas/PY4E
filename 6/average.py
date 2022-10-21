count = 0
sum = 0
print("Before", count, sum)
for number in [13, 43, 64, 6, 11, 43, 12, 15, 17]:
    count = count + 1
    sum = sum + number
    print(count, sum, number)
print("After", count, sum, round(sum / count, 1))
