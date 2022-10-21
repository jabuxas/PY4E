counts = dict()
names = ["fang", "su", "han", "zhang", "moretti", "fang", "su", "fang", "wang"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
    # if name not in counts:
    #     counts[name] = 1
    # else:
    #     counts[name] += 1
print(counts)
