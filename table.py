choice = "yes"
while choice != "no":
    num = int(input("Enter a number: "))
    i=1
    while i<=8:
        print(num, "*", i, "=", num*i)#
        i+=1

    choice = input("Enter your choice: ")
