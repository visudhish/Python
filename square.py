#This program displays square upto given numbers
Givennumber = int(input("Enter a given number : "))
for number in range(1,Givennumber+1,1):
    square = number*number
    print("square of",number,"is",number,"x",number ,"=", square )
#end program