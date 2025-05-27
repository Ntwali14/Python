def calculator(n1,n2,opr):
    def add():
        return n1+n2
    def sub():
        return n1-n2
    def mul():
        return n1*n2
    def div():
        return n1/n2
    
    if opr == '+':
        print(f'Result is {add()}')

    elif opr == '-':
        print(f'Result is {sub()}')

    elif opr == '*':
        print(f'Result is {mul()}')

    elif opr == '/':
        print(f'Result is {div()}')

def main():
    num1 = float(input('ENter first number: '))
    num2 = float(input('Enter second number: '))
    opr = input('Enter operator: ')
    calculator(num1,num2,opr)
main()