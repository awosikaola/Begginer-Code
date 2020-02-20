password = ''
while password != 'password123':
    password = (input('enter your passcode: '))
    if (password == 'password123'):
        print('you are logged in')
    else:
        print('Sorry try again')