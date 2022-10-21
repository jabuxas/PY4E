# Enviroment Variables
ggg = dict()
lenv = list()
lvalue = list()

while True:
    env = input("Enviroment variables: ")
    if env == "exit":
        quit()
    env = env.split()
    key = env[0]
    value = env[1]
    lvalue.append(value)
    lenv.append(key)
    for i in range(len(lvalue)):
        ggg.update({lenv[i]: lvalue[i]})
    print(ggg)
