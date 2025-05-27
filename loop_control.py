#program to find the sum of digits

num= int(input("Enter any number: "))

s = 0
while num!=0:
    r = num%10
    s += r
    num = num//10
print("Sum of digits is: ", s)
