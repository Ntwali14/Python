print("*****CALCULATOR******")
print("1.Add")
print("2.Subtract")
print("3.Divivde")
print("4.Multiply")
print("5.Modulus")
opt = int(input("Enter your option: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match(opt):
    case 1:
        print("The sum is ", num1+num2)
    case 2:
        print("The difference is ", num1-num2)
    case 3:
        if num2 != 0:
            print("The quotient is ", num1/num2)
        else:
            print("Can not divide by zero!!!")
    case 4:
        print("The product is ", num1*num2)
    case 5:
        print("The remainder is ", num1%num2)
    case _:
        print("Invalid option")

