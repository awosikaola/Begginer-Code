def max_of_two(x,y):
    if x>y:
        return x
    return y

def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))

a= input('enter value for x: ')
b= input('enter value for y: ')
c= input('enter value for z: ')

print(max_of_three(a,b,c))