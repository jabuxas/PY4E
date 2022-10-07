# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
all = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = line.find(" ")
    line = line[num + 1 :]
    line = line.rstrip()
    all = all + float(line)
    count += 1
print("Average spam confidence:", all / count)
