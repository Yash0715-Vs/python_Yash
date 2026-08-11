a=[1,2]
b=[1,2]
c=a.copy()
print(c==a) #true coze list value are same
print(a==b) # true because list values are same
print(c is a) #false because diff list objs
print(a is b) #false because diff list objects
print(id(a))#id of a
print(a is not b)# true because diff list objs