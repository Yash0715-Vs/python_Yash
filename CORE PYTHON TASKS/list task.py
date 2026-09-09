a=[1,'a',2,'b',3,4,55,'asit','nimesh']

str_List =[]#empty list
for i in a:
    if isinstance(i,str): # use to check if the element is a string or not
        str_List.append(i) # add the string element to the str_List
        
print(str_List)

int_List =[] #empty list
for i in a:
    if isinstance(i,int): # use to check if the element is an integer or not
        int_List.append(i) # add the integer element to the int_List

print(int_List)
print(max(int_List))
print(min(int_List))
