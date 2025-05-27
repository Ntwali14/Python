#program to check if input is alphabet, digit or special character

ch = input("enter any character: ")
if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
    print(ch," is alphabet")
elif ch>='0' and ch<='9':
    print(ch," is a digit")
else:
    print(ch, "is a special character")

'''ASCII code
    a=97
    A=65
    0=48
'''