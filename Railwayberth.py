
#This program displays Type of berth
berthno = int(input("Enter Berth no : "))
Typeofberth = berthno%8
if (Typeofberth==1 or Typeofberth == 4):
    print("lower berth")
elif (Typeofberth==2 or Typeofberth==5):
    print("middle berth")
elif (Typeofberth==3 or Typeofberth ==6):
    print("upper berth")
elif Typeofberth==7:
    print("side lower")
elif Typeofberth==8:
    print("side upper")
else:
    print("invalid")
#end program


