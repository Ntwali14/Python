def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
def main():
    num = int(input('Enter any number: '))
    res = factorial(num)
    print(f'Factorial is {res}')
main()