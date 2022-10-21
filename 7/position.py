data = "From jader.theisges@ufsc.com.br Sat Jan  5 09:15:16 2020"
atpos = data.find("@")
endpos = data.find(" ", atpos)
host = data[atpos + 1 : endpos]
print(host)
