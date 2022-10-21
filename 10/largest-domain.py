name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
largestK = None
largestV = None
for line in handle:
    if line.startswith("From "):
        words = line.split()
        domain = words[1]
        domain = domain.split("@")
        counts[domain[1]] = counts.get(domain[1], 0) + 1
print(counts)
