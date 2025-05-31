#Email Book Application
email_set=set()
while True:
    print('***Email Book***')
    print('1. Add Email')
    print('2. Remove Email')
    print('3. Search Emails')
    print('4. List Emails')
    print('5. Exit')

    case = int(input('Enter your choice: '))

    if case == 1:
        email_id=input('Enter email to add: ')
        if email_id in email_set:
            print('This email id already exists')
        else:
            email_set.add(email_id)
    elif case == 2:
        email_id=input('Enter email to remove: ')
        if email_id in email_set:
            email_set.remove(email_id)
            print('Email removed successfully')
        else:
            print('Email not found')
    elif case == 3:
        email_id=input('Enter email to search: ')
        if email_id in email_set:
            print(email_id, 'Email found')
        else:
            print(email_id, 'Email not found')
    elif case == 4:
        for email_id in email_set:
            print(email_id)
    elif case == 5:
        print('Exiting the application...')
        break