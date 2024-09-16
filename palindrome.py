

#This program reverse the digits of a number
Number = int(input("Enter a number : "))
OriginalNumber = Number
product=0
while Number>0:
    print("Number is " ,Number)
    Reminder = Number%10
    print("Reminder is ", Reminder)
    print("product is",product,"* 10 +",Reminder)
    product =product*10+Reminder

    print("Product is",product)
    Number=int(Number/10)
print(product)
if(product == OriginalNumber):
    print("true")
else:
    print("false")
#end program