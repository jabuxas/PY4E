def computepay(h, r):
    if float(h) <= 40:
        pay = float(h) * float(r)
        print(pay)
    else:
        overr = float(r) * 1.5
        overp = float(h) - 40
        pay1 = overp * overr
        pay2 = float(r) * 40
        payfinal = pay1 + pay2
        return payfinal

hour = input("How many hours? ")
rate = input("How much is the rate? ")
print("Pay", computepay(hour, rate))
