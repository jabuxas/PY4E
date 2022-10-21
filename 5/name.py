def hello(name):
    print("Hi,", name)

expect = input("What is your name? ")
hello(expect)

def greet(lang, vulgo):
    if lang == 'pt':
        print("Olá,", vulgo)
    elif lang == 'ko':
        print("Annyeonghaseyo,", vulgo )
    else:
        print("Hello,", vulgo)

lang = input("What language do you speak? ")
vulgo = expect
greet(lang, vulgo)
