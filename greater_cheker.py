a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b:
    if a>c:
        print(a, " is max")
    else:
        print(c, " is max")
elif b>c:
    if b>a:
        print(b, " is max")
    else:
        print(a, " is max")
elif c>a:
    if c>b:
        print(c, " is max")
    else:
        print(b, " is max")

else:
    print("Is equal")
