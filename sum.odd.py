# Numint1 = int(input("enter number1 :"))
# Numint2 = int(input("enter number2 : "))
# sum = 0
# for num in range(Numint1,Numint2,2):
#    sum += num#    print(sum)
#This program displays Average of numbers until given number .   
num = int(input("Enter a number : "))
sum = 0
for i in range(1,num+1):
    sum = i+sum
Average = sum/num
print("sum : ",sum)
print("Average of numbers until given number is",Average)
#end program
    
    