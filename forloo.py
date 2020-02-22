temp =[12,49.-270,40]
def celtofa(temp):
    with open("temp.txt", 'w') as file:
        for c in temp:
            if c> -273:
                f=c*9/5+32
                file.write(str(c)+"\n")
print (celtofa(temp))