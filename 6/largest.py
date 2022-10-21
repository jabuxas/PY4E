num = -1
print("Before", num)
for i in [13, 643, 756, 234, 723, 876, 12, 35, 754, 312, 910, 132, 528]:
    if i > num:
        num = i
    print(num, i)
print("The largest is:", num)

# Could also be writen as:
# num = None
# print("Before", num)
# for i in [13, 643, 756, 234,723, 876, 12, 35, 754, 312, 910, 132, 528]:
#     if num is None:
#         num = i
#     if i > num:
#         num = i
#     print(num, i)
# print("The largest is:", num)
