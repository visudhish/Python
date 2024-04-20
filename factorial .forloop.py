#initilisation 
number = input("Enter a number : ")
numberint = int(number)
#endinitilisation
#factorial logic
factorial = 1
for num  in range(numberint,1,-1):
    factorial = factorial*num
#end logic 
print("factorial of",numberint,"is",factorial)
#end
