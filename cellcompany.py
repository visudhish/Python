#initilisation
callduration = input("call duration in sec:")
calldurationint = int(callduration)
Month = input("no of days in month:")
monthint = int(Month)
#endinitilisation
#logic
if (calldurationint <= 500):
    charge = calldurationint*0.01*monthint
    print("Total amount :", charge,"$")
elif (calldurationint <= 800):
    charge = calldurationint*0.008*monthint
    print("Total amount :",charge,"$")
else:
    charge = calldurationint*0.005*monthint
    print("Total amount :",charge,"$")

#end                
