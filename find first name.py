1.#code displays user's first name
username ="sudhish simhadri"
first_name = username.split()[0]
print(first_name)
#end program
2.#code displays greatest among three numbers
num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))
if (num1>num2):
  greaternumber=num1
else:
  greaternumber=num2
if (greaternumber>num3):
  print(greaternumber,"is greatest")
else:
  print(num3,"is greatest")
