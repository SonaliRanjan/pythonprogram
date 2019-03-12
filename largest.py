num1=int(input("Enter first no.:"))
num2=int(input("Enter 2nd no.: "))
num3=int(input("Enter 3rd no.: "))

if (num1>=num2) and (num1>=num3):
	print("largest no.is",num1)
elif (num2>=num1) and (num2>=num3):
	print("largest no. is ",num2)
else:
	print("largest no. is ",num3)