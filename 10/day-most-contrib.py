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
        counts[words[2]] = counts.get(words[2], 0) + 1
print(counts)
# If want to see largest uncomment below :
# for k, v in counts.items():
#     if largestV is None or largestV < v:
#         largestK = k
#         largestV = v
# print(largestK, largestV)
