print ("Hello, welcome here")
val = input("What will you like to do? Enter A for Addition, M for Multiplication, D for Division and S for subtraction: ")
if val == "A":
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(a+b)
    print("The sum of the values entered is " +str(c))
elif val == "M":
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(a*b)
    print("The product of the values entered is " +str(c))
elif val == "D":
    a = float(input("Enter value 1: "))
    b = float(input("Enter value 2: "))
    c = float(a/b)
    print("The division of the values entered is " +str(c))
elif val == "S":
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(a-b)
    print("The subtraction of the values entered is " +str(c))
else:
    print("I don't understand your input")
    