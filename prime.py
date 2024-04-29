#This program Displays given number is prime or composite
Givennumber = int(input("Given number : "))
factorcount = 0
for loopvariable in range(1,Givennumber+1):
  if Givennumber % loopvariable==0:
     factorcount = factorcount+1
     
print(factorcount)
if factorcount == 2:
   print("prime number")
else:
   print("composite")
#end program

   