#This program displays a number and the sum of the digits of the number
number = int(input("Enter a number : "))
quotient = int(number)
sum=0
while quotient > 0:
    reminder = quotient%10
    sum= sum+reminder
    quotient=quotient/10
print(number,"sum of the digits in the number",sum)
