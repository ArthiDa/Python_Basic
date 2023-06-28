import os
os.system('cls')
a = "Hello, World!"
print(a[4])

l = len(a)
print(l)
#for x in a:
    #print(x)
print("ll" in a)
b = int(input("Enter a number: "))
os.system('cls')
if "lld" in a:
    print("YES ll present in a")
else:
    print("No")

cn=0
for x in a:
    if x=='l':
        cn+=1

print(cn)