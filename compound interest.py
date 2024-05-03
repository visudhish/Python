#This program displays compound interest and simple interest
P = int(input("Enter principal amount :"))
R = int(input("Enter interest per annum : "))
T = int(input("Enter number of years : "))
simpleinterst = (P*T*R)/100
compoundinterest = P*pow((1+(R/100)),T)-P
print("simple intrest is",simpleinterst)
print("compound intrest is",compoundinterest)
#end