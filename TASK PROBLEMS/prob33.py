a = 100 #Python (specifically CPython) usually caches integers from -5 to 256.
b = 100

print(a == b)
print(a is b)

x = 500 
y = 500

print(x == y)
print(x is y)#Python is allowed to reuse objects as an optimization.
# In some environments,the compiler may make both x and y refer to the same 500 object.