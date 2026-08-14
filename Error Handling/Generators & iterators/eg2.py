def count_up(n):
    for i in range(1, n + 1):
        yield i


n = int(input("Enter n: "))

for num in count_up(n):
    print(num)