import math
num1,num2 = map(int,input().split())


print("floor "+str(num1)+" / "+str(num2)+" = "+str(math.floor(num1/num2)))
print("ceil "+str(num1)+" / "+str(num2)+" = "+str(math.ceil(num1/num2)))
print("round "+str(num1)+" / "+str(num2)+" = "+str(round(num1/num2)))



# floor 10 / 3 = 3
# ceil 10 / 3 = 4
# round 10 / 3 = 3