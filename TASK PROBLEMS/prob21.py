a = [2,3,4,1]
b= [2,1,3]
set1 = set(a) #we convert list into set
set2 =set(b)
print(f"union: {set1|set2}")
print(f"intersection: {set1 & set2}")
print(f"difference: {set1 -set2}")

unique = set1 |set2
print(unique)

sorting= sorted(unique) #convert set into list
print(sorting)
