camels = 42
d = "I have spotted %d camels" % camels
print(d)

print("I love %(language)s" % {"language": "Python"})

ask = input("Who do you love? ")
print("You love %(ask)s" % {"ask": ask})
