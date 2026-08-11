# Create a list of 10 

l =[1,2,3,3,5,6,7,8,9,10]


print(f"Largest number: {max(l)}") #greater
print(f"Smallest number: {min(l)}")#lower


l = list(set(l)) #because sat dosent allowed duplicate values
print(f"After removing duplicates: {l}")

l.sort() #sort the list
print(f"Sorted list: {l}")