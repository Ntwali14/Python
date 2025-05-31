'''a=[10,10]
print(type(a))
print(a)'''

'''b={10,10,'john',10.5,True}
print(b)'''

b={10,10,'john',10.5,True}
b.add(20)
b.add(10)
b.remove(10.5)
b.update([30, 40])
b.discard('john')
b.clear()
print(b)
