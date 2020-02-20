temp = [10,-20,-289,100]
def cel_to_fah(cel):
    fah = cel*9/5+32.0
    return fah

cel = float (input("Enter the temperature in Celsius: "))

if cel>-213.5:
    print(cel_to_fah(cel))
else:
    print('it does not make sense')
