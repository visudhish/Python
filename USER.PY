#Initilisation
user = input("member(Y/N): ")
user =user.capitalize()
memberpercentage = 10
nonmemberpercentage = 20
memberchargeindollars = 2
nonmemberchargeindollars = 5
#endinitilisation

if(user == "Y"):
    
    userspenthours = input("no.of hours spent:")
    ushint = int(userspenthours)
    payindollars = memberchargeindollars*ushint
    Tax = payindollars*memberpercentage/100
    Totalamount = payindollars+Tax
    print("The User is a Member stayed",ushint,"hours for",nonmemberchargeindollars,"per hour plus",memberpercentage , "total amount is",Totalamount)
elif(user=="N"):
    userspenthours = input("no.of hours spent:")
    ushint = int(userspenthours)
    payindollars = nonmemberchargeindollars*ushint
    Tax = payindollars*nonmemberpercentage/100
    Totalamount = payindollars+Tax
    print("The user is  not a member",ushint,"hours for ",nonmemberchargeindollars," per hour plus",nonmemberpercentage ," total amount is",Totalamount)
else:
    print("Invalid Input")