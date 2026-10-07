# Declaration of variables for the entire program's operation

true_login = 'abcd'
true_password = 1234

# Implementation of a data validation mechanism that retrieves operational values and modifies the user-provided password type to avoid conflicts

while True:
    print('LOGIN TO YOUR ACCOUNT\n')
    user_login = input('• Login: ')
    user_password = input('• Password: ')
    if user_login == true_login and user_password == str(true_password):
        print('\nLOGIN SUCCESSFUL')
        break
    else:
        print('\nLOGIN FAILED. TRY AGAIN\n')
        continue