#Write a Python program that counts the number of digits in a given integer.

def count_digits(n):
    n = abs(n)

    count = 0

    while n > 0:
        n //= 10
        count +=1
    return count

num = int(input('Enter any integer: '))
print(f'The number of digits in {num} is {count_digits(num)}')