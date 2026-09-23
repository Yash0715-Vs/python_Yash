y=[]
def find_prime(n):
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            y.append(i)
    return y
n=20
result = find_prime(n)
print(result)