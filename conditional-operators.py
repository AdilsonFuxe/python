validEmail = 'mail@mail.com'
validPassword = '123456'

email = raw_input('enter your email?: ')
password = raw_input('enter your password?: ')

if validEmail == email and validPassword == password:
    print 'Welcome Adilson Fuxe!'
else:
    print 'Invalid email or password!'
