d1 ={"a":1, "b":2, "c":4}
d2 ={"b":3,"d":5}

for key in d2:
    if key in d1:
        d1[key] = d1[key] + d2[key]
    else:
        d1[key] = d2[key]

print(d1)

