#This program displays min of 10 given numbers
min = 100
for loopvariable in range(1,11):
    n = int(input("Enter a number : "))
    if n < min:
        min = n
print(min)
#end program