def string_to_lenght(mystring):
    if type(mystring) == int:
    return ("sorry ints don't have lenghts")

        else:
            return len(mystring)
    ##newstr = len(mystring)
    ##return newstr

mystring = str (input("Enter your string to calculate the lenght: "))

print (string_to_lenght("mystring"))