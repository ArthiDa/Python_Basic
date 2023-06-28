x = "Hello World"
print(type(x))
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j #sqrt(-1)
print(type(x))
x = ["Apple","Banana"] #list
print(type(x))
x = ("Apple","Banana") #tuple
print(type(x))
x = range(6)
print(type(x))
x = {"Name":"John","age":35}
print(type(x))
x = {"apple","banana"}#set
print(type(x))
x = frozenset({"Apple","Banana"})
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(x)
print(type(x))
x = memoryview(bytes(5))
print(x)
print(type(x))

#Numbers
x = 1 #int
y = 2.8 #float
z = 1j #complex
#convert from int to float
a = float(x)
#convert from float to int
b = int(y)
#convert from int to complex
c = complex(x)
print(a)
print(b)
print(c)
print(z+c)
#Random Number
import random
print(random.randrange(1,10))