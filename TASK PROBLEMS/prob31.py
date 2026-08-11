s = "yash is a good yash is also great"

result = []

for word in s.split():
    if word not in result:
        result.append(word)

print(" ".join(result))