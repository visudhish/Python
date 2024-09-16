#This program displays the vowel in given string.
string = "km"
vowels = ["a","e","i","o","u"]
vowelfound = False
for letter in string:
    if vowels.__contains__(letter):
      print (letter)
      vowelfound = True
#check if still vowelfound is false after the loop    
if vowelfound == False:    
    print("no vowels")
#end program


