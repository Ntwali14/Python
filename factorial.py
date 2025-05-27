num=int(input("Enter any number: "))

fact = 1

while num>0:
    fact = fact*num
    num-=1
print("The factorial is ", fact)