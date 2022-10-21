def computegrade(grade):
    if float(grade) >= 0.9:
        grade = 'A'
    elif 0.9 > float(grade) >= 0.8:
        grade = 'B'
    elif 0.8 > float(grade) >= 0.7:
        grade = 'C'
    elif 0.7 > float(grade) >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    print(grade)

gradeinput = input("Enter score: ")
computegrade(gradeinput)

