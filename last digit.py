# #initilisation
# Number=input("number:")
# Numberint=int(Number)
# #endinitilisation
# #logic
# lastdigit=(Numberint%10)
# print("lastdigit is",lastdigit)
# #end

#initilisation
numberofhours=input("number of hours worked:")
numberofhoursint=int(numberofhours)
hourlyincome=input("income per hour:")
hourlyincomeint=int(hourlyincome)
ps4cost=input("ps4cost:")
ps4costint=int(ps4cost)
Tvcost=input("Tv cost:")
Tvcostint=int(Tvcost)
Gameskin=input("Gameskin:")
Gameskinint=int(Gameskin)
#endinitilisation
#logic
totalincome=(numberofhoursint*hourlyincomeint)
Totalcostofgadgets=(ps4costint+Tvcostint+Gameskinint)
if(totalincome>Totalcostofgadgets):
    print("I can buy all gadgets")
else:
    print("I cannot buy all the items") 
#end   

