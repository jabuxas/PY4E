fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    sentence = line.split()
    for word in sentence:
        if not word in lst:
            lst.append(word)
    lst.sort()
print(lst)
