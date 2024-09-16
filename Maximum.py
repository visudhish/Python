#This program displays max number among given 10 numbers
max = 0
for loopvariable in range(1,11,1):
    number = int(input("Enter a number : "))
    if (number > max):
        max = number
        
print("max num is",max)
#end     

