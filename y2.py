a1 = int(raw_input())
a2 = int(raw_input())
a3 = int(raw_input())
# uncomment following lines to take three numbers from user
#a1 = float(input("Enter first number: "))
#a2 = float(input("Enter second number: "))
#a3 = float(input("Enter third number: "))
if (a1 >= a2) and (a1 >= a3):
   largest = a1
elif (a2 >= a1) and (a2 >= a3):
   largest = a2
else:
   largest = a3
print(largest)
