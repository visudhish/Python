#This program Displays given number is prime or composite
Givennumber = int(input("Given number : "))
factorcount = 0
for loopvariable in range(1,Givennumber+1):
  if Givennumber % loopvariable==0:
     factorcount = factorcount+1
     
print("factorcount is",factorcount)
if factorcount == 2:
   print(" number is prime number")
else:
   print("number is composite")
#end program

