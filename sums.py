a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))

def sum(a,b,c):
	sum=a+b+c
	if a==b or b==c or c==a:
		sum=0
	return sum
print("sum of 3 numbers is:",sum(a,b,c))