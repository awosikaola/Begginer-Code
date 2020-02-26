print ("Hello, welcome here")
val = input("What will you like to do? Enter A for Addition, M for Multiplication, D for Division and S for subtraction: ")
if val == "A":
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(a+b)
    print(c)
elif val == "M":
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(a*b)
    print(c)
elif val == "D":
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(a/b)
    print(c)
elif val == "S":
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(a-b)
    print(c)
else:
    print("I don't understand your input")
    