#percentage program
# This program will take a percentage as input and return the corresponding letter grade.
# The grading scale is as follows:
# A: >90
# B: >80 and <=90
# C: >=60 and <=80
# D: below 60

num = int(input("enter a number between 0 and 100: "))

if num > 90 and num:
    print("The Student's grade is A")
elif num > 80 and num<=90:
    print("The Student's grade is B")
elif num >= 60 and num <= 80:
    print("The Student's grade is C")
elif num < 60 and num >= 0:
    print("The Student's grade is D")
else:
    print("Invalid input, please enter a number between 0 and 100")
