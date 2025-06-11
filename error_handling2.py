def multiply(n1,n2):
    if n1==0 or n2==0:
        raise ValueError()
    else:
        return n1*n2
def  main():
    num1 = int(input('enter first number: '))
    num2 = int(input('enter second number: '))
    try:
        num3 = multiply(num1, num2)
        print(f'result is {num3}')
    except ValueError:
        print('gives zero')

main()