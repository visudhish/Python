#initilisation
Dow=input("Data consumed on wikipedia:")
Mow=input("Data consumed on memes:")
Covw=input("cost of visiting wikipedia:")
Cowm=input("cost of watching movie:")
Dowint=int(Dow)
Mowint=int(Mow)
Covwint=int(Covw)
Cowmint=int(Cowm)
#endinitilisation
#logic
Totalconsumption=(Dowint+Mowint)
if(Totalconsumption>100):
    print("To much consumpution")
if(Cowmint>Covwint):
    print("wow so many memes,lol")        