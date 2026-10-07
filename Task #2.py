# Announcement of the lists
login_list = []
password_list = []

# Test

# Creating a basic cycle
while True:

    # Formation of the initial selection mechanism
    print('THE BLACKNET SYSTEM WELCOMES YOU')
    print('To get started, register or log in to the system')
    print('1 - registration, 2 - login\n')
    choice = input('Select one of the two available functions by entering the corresponding value: ')

    # Creation of a registration mechanism
    if choice == '1':
        print('\nCREATING A NEW ACCOUNT\n')
        user_signup_login = input('Create your own login: ')
        login_list.append(user_signup_login)
        user_signup_password = input('Create your own password: ')
        password_list.append(user_signup_password)
        print('Account successfully created')
        continue

    # System login mechanism architecture
    elif choice == '2':
        print('\nLOG IN TO AN EXISTING ACCOUNT\n')
        user_login_login = input('Login: ')
        user_login_password = input('Password: ')
        if user_login_login == login_list[0] and user_login_password == password_list[0]:
            print('Successfully logged into the account')
        else:
            print('Account not found')
            continue
    else:
        print('Select only one of the available values')