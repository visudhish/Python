#initilisation
laptopprice=input("laptop price:")
Tax=input("Tax%:")
laptoppriceint=int(laptopprice)
Taxint=int(Tax)
Totalprice=((laptoppriceint/100)*Taxint)+laptoppriceint
print("Total price of laptop is",Totalprice)
#end