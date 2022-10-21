smallest = None
print("Before", smallest)
for number in [5, 64, 52, 7, 4, (-5), (-2), (-9), 32]:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    print(smallest, number)
print("After", smallest)

