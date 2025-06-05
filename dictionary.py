'''course_dict = {'name':'John Doe','rollno':20,'marks':85} 
print(course_dict['name'])

for n in course_dict:
    print(n, ":", course_dict[n])'''

#updating the dictionary
d1={1:100, 2:344, 3:245}
print(d1)

d1.update({1:20, 2:222, 3:333})
print(d1)

d1.popitem()
print(d1)

del d1[1]
print(d1)

'''d1.clear()
print(d1)'''