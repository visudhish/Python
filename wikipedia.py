#initilisation
Dow=input("Data consumed on wikipedia in Mbps:")
Mow=input("Data consumed on memes in Mbps:")
Covw=input("cost of visiting wikipedia in $:")
Cowm=input("cost of watching memes in $:")
Dowint=int(Dow)
Mowint=int(Mow)
Covwint=int(Covw)
Cowmint=int(Cowm)
#endinitilisation
#logic
Totalconsumption=(Dowint+Mowint)
if(Totalconsumption>100):
    print("Too much consumpution")
if(Cowmint>Covwint):
    print("wow so many memes,lol")        