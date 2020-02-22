file = open("test.txt", 'w')
number=[1,2,3,4]
for i in number:
    file.write(str(i)+"\n")
#file.write(str([1,2,3])+"\n")
print(file)