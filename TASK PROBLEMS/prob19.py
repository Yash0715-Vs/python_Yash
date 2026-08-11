


a= [1,2,3,4]
b= [1,2,3,4]

print(a==b) #true
print(a is b)#false
print(id(a))#id of a
print(id(b))#id of b

c=a #create a new one list
print(id(c))#id of c 

a.append(5)# add the value in list
print(a)
c=a.copy()#create a copy of list 
print(c)

print(id(a))#id of a
print(id(b))#id of b
print(id(c))#id of c