fhand = open("lorem.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)
