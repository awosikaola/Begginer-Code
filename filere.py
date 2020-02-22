file = open("fruits.txt", 'r')
content= file.read()
file.close()
for i in content:
    print(len(i.strip()))