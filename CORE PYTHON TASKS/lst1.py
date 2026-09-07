
ls = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6, ['d', 'e', 'f'], 7, 'g', 8, 'h', [9, 10, 'i', 'j'], 11, 'aansh']

for i in ls:
    if isinstance(i, list): #use to check if the element is a list or not
        for j in i:  #Run loop for elements inside the nested list
            print("\t", j) #\t is a tab space in python 
    else:
        print(i)