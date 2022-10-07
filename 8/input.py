fname = input("What is the name of the file? ")
try:
    fhand = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    print("Could not open file:", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", fname)
