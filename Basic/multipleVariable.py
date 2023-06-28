x,y,z = "Arthi","Pritam",10
a = b = c = "Pranab"
print(x)
print(y)
print(z)
print(a+" "+b+" "+c)

fruits = ["Apple","Banana","Cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

x = 5
y = "John"
# print(x+y)
# combine a string and a number with
# the + operator,
# Python will give you an error
print(x,y)

x = "Arthi Barua"
print(x)

#global variables
x = "Arthi"
def myfunc():
    print("My name is "+x)
myfunc()

x = "Arthi"
def func():
    x = "Pranab"
    print("My name is "+x)
func()
print("My name is",x)

x = "awesome"
def example():
    global x
    x = "fantastic"
example()
print("Python is "+x)