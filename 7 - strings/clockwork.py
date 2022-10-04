text = "X-DSPAM-Confidence:    0.8475"
n = text.find("0")
number = text[n:]
print(float(number))
