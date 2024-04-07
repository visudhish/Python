#initilisation
Geometry=input("geometrymarks:")
algebra=input("algebramarks:")
physics=input("physicsmarks:")
Geometryint=int(Geometry)
algebraint=int(algebra)
physicsint=int(physics)
#endinitilisation
#Average marks
import statistics;
print("avg is",statistics.mean([Geometryint,algebraint,physicsint]))
#end