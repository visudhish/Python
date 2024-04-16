#Initilisation
Productcost = input("Cost of the Product:")
PCint = int(Productcost)
Location = input("Location name:")
if(Location== "USA"):
    payindollars = PCint+5
    payint = int(payindollars)
    print("you have to pay",payint,"in dollars")
elif(Location =="Europe"):
    payindollars = PCint+7
    payint = int(payindollars)
    print("youhave to pay",payint,"in dollars")
elif(Location == "Canada"):
    payindollars = PCint+3
    payint = int(payindollars)
    print("you have to pay",payint,"in dollars")
    
else:
    payindollars=PCint+9
    payint = int(payindollars)
    print("youhave to pay",payint,"in dollars")
#end