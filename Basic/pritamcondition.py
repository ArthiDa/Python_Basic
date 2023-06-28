a = int(input())
b = int(input())
c = int(input())

# int mx = 0,mn=0,mid=0
[mx,mn,mid] = [0,0,0]


# jodi b and c theke a boro 
if a > b & a > c:
    mx = a
    if b > c:
        mid = b
        mn = c
    else:
        mid = c
        mn = b
# jodi a and c theke b boro 
elif b > a & b > c:
    mx = b
    if a > c:
        mid = a
        mn = c
    else:
        mid = c
        mn = a
# jodi a and b theke c boro 
else:
    mx = c
    if a > b:
        mid = a
        mn = b
    else:
        mid = b
        mn = a
print("Max number is: ",mx)
print("Mid number is: ",mid)
print("Minimum number is: 6",mn)
    
