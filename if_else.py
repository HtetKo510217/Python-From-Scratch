# age = int(input('age : '))

# if age < 18:
#     print('you are young')
# elif age > 18 and age < 30:
#     print('You are normal age')
# else:
#     print('You are old')

# Login check

userName = "htetko"
password = 'admin123'

loginUser = input('Enter your name : ')
LoginPassword = input('Enter your password : ')


if userName == loginUser and password == LoginPassword:
    print('Login success')
elif userName != loginUser and password == LoginPassword:
    print('Wrong user name')
elif userName == loginUser and password != LoginPassword:
    print("Wrong Password")
else:
    print('Wrong User name and password')
