#no arguments but with return value
'''def func():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return (a+b)

def main():
    result = func()
    print(f"The result is {result}")

main()'''

#with arguments but no return value
'''def add(a,b):
    print("The sum is: ", a+b)
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    add(num1,num2)
main()'''

#with arguments and return values
def add(a,b):
    return a+b

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Eenter second number: "))
    result = add(num1,num2)
    print(f"The sum is {result}")
main()