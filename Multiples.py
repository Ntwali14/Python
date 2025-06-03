#Write a Python program that checks if a number is a multiple of another number.

def is_multiple(num1, num2):

    if num1 % num2 == 0:
        return True
    else:
        return False
    
# Example usage
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(f'Is {num1} a multiple of {num2}? {is_multiple(num1, num2)}')
# This program checks if the first number is a multiple of the second number.