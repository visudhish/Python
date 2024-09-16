# #initilisation
# laptopprice=input("laptop price:")
# Tax=input("Tax%:")
# laptoppriceint=int(laptopprice)
# Taxint=int(Tax)
# Totalprice=((laptoppriceint/100)*Taxint)+laptoppriceint
# print("Total price of laptop is",Totalprice)
# #end

#initilisation
minimumwage=input("minimum wage:")
yearsemployed=input("No.of years employed:")
bonus=input("Bonus per year:")
numberofchildren=input("no.of children:")
bonusperchild=input("bonus per child:")
minimumwageint=int(minimumwage)
yearsemployedint=int(yearsemployed)
bonusint=int(bonus)
numberofchildrenint=int(numberofchildren)
bonusperchildint=int(bonusperchild)
#endinitilisation
#logic
Totalbonus=(yearsemployedint*bonusint)+(numberofchildrenint*bonusperchildint)
print("Total salary is:",minimumwageint+Totalbonus)
#end



                    
