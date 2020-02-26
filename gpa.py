classes = []
grades = []
#print("This is a program to get and calculate your GPA")
def gpa():
    i=0
    while (i <= 10):
        course = input("Enter the course name")
        classes.append(course)
        i = i+1

    print(classes)
    y=0
    while (y<=10):
        grade = input("Enter the grade for each courses entered")
        grade = grade.upper()
        grades = grade.append()
        y = y+1
    calculate()

def calculate():
    total = 0
    for element in grades:
        if element == "A":
            total = total + 5.0
        elif element == "B":
            total = total + 4.0
        elif element == "C":
            total = total + 3.0
        elif element == "D":
            total = total + 2.0
        elif element == "E":
            total = total + 1.0
        elif element == "F":
            total = 0
    gpas = total/6
    print(gpas)

#collect()