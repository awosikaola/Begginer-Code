def sum(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print (sum((8,5,7,3,7)))