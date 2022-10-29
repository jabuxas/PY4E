c = {"a": 10, "b": 1, "c": 4, "d": 13}
tmp = list()
for k, v in sorted(c.items()):
    tmp.append((v, k))
print(tmp)
# if we want to reverse the order (sort by biggest to the smallest)
tmp = sorted(tmp, reverse=True)
print(tmp)
