a= 22
b= 22.7
c= "Yash"
d= [1,2]
e=(3,4)
f={5,6}
g={"yash":22}
h=(a>b)

print(type(a))
print("Operation:", a + 5)
print("Mutable: No (Immutable)")
print("ID:", id(a))

print(type(b))
print("Operation:", b * 2)
print("Mutable: No (Immutable)")
print("ID:", id(b))

print(type(c))
print("Operation:", c.upper())
print("Mutable: No (Immutable)")
print("ID:", id(c))

print(type(d))
d.append(40)
print("Operation:", d)
print("Mutable: Yes")
print("ID:", id(d))

print(type(e))
print("Operation:", e + (4,))
print("Mutable: No (Immutable)")
print("ID:", id(e))

print(type(f))
f.add(4)
print("Operation:", f)
print("Mutable: Yes")
print("ID:", id(f))

print(type(g))
g["City"] = "Ahmedabad"
print("Operation:", g)
print("Mutable: Yes")
print("ID:", id(g))


print(type(h))
print("Operation:", not h)
print("Mutable: No (Immutable)")
print("ID:", id(h))
