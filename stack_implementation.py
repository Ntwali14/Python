#program to show the working and implementation of a stack data structure using Python

'''stack = []

while True:
    print('******Stack Operations*******')
    print('1. Push')
    print('2. Pop')
    print('3. View')
    print('4. Exit')

    opt = int(input('Choose operation: '))
    match(opt):
        case 1:
            n = int(input('Enter elements to push: '))
            stack.append(n)
            print(n, 'is pushed inside the stack')
    
        case 2:
            if len(stack) == 0:
                print('Stack is empty, cannot perform operation')
            else:
                n=stack.pop()
                print(n, 'is popped from the stack')
    
        case 3:
            print('Stack is ', stack)

        case 4:
            break

        case _:
            print('Invalid operation!! Try again')'''




stack  = []

while True:
    print('***Choose operation')
    print('1. Push')
    print('2. Pop')
    print('3. View')
    print('4. Exit')

    case = int(input('Choose operation: '))

    if case == 1:
        n = int(input('Enter values to be pushed into stack: '))
        stack.append(n)
        print(n, 'has been pushed into stack')
    elif case == 2:
        if len(stack)==0:
            print('Stack is empty so the operation can not be executed')
        else:
            n = stack.pop()
            print(n, 'has been popped from the stack')
    elif case == 3:
        print('Stack: ', stack)
    elif case == 4:
        print('Exiting Stack...')
        break
