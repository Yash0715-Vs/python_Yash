l= [1,2,2,3,3,6,4,2,8,7]

print(f"Largest number: {max(l)}") #greater
print(f"Smallest number: {min(l)}")#lower
print(f"sum: {sum(l)}")
avg = sum(l)/len(l)
print(f"the avg is: {avg}")
l = list(set(l)) #because sat dosent allowed duplicate values
print(f"After removing duplicates: {l}")
l.sort()
print(f"the sorted list: {l}")
