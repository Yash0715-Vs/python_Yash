a=[1,2]
b=[1,2]
print(a==b) # true because list values are same
print(a is b) #false because diff list objects
print(id(a)) #id
print(id(b))
c=a
a.append(3)
print(c)