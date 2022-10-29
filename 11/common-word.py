# top ten common words
fhand = open("romeo.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# all code under can be summarized to:
# print(sorted([(v, k) for k, v in counts.items()], reverse=True))
lst = list()
for k, v in counts.items():
    newtup = (k, v)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

for k, v in lst[:10]:  # only the top 10
    print(v, k)
