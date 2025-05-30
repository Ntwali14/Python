#program to sort a list of values into even and odd

n = [1,3,45,23,22,4,6,87,34,56,34,56,34,21,43,76,46,67,24,90,94,]

even_list=[]
odd_list=[]

for n in n:
    if n%2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print(f'List of even numbers {even_list}')
print(f'List of odd numbers {odd_list}')