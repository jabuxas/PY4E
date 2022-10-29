dc = dict()

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    time = time.split(":")
    dc[time[0]] = dc.get(time[0], 0) + 1

lst = list()
for k, v in dc.items():
    newtup = (k, v)
    lst.append(newtup)
lst = sorted(lst)

for k, v in lst:
    print(k, v)
