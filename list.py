def currency_change(rate, dollar):
    naira = rate*dollar
    return naira

r= input('Enter the exchange rate from naira to dollar: ')
d= input('How much dollar are you changing?: ')

print("The total amount is {}").format(currency_change(float(r), float(d)))
