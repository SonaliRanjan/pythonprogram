import random
l=["rock","paper","scissor"]
us=0
cs=0
while True:
	# take input from user
	u=input("enter your choice,press n to discontinue")
	# to exit 
	if u=='n':
		print("game over")
		exit()
	#input from computer
	c=random.choice(l)
	print("computer chooses",c)
	#compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="rock" and c=="paper":
		cs=cs+1
		print("comp score",cs)
		print("user score",us)
	elif  u=="rock" and c=="scissor":
		us=us+1
		print("user score",us)
		print("comp score",cs)
	elif u=="paper" and c=="rock":
		us=us+1
		print("user score",us)
		print("comp score",cs)
	elif u=="paper" and c =="scissor":
		cs=cs+1
		print("comp score",cs)
		print("user score",us)
	elif u=="scissor" and c=="paper":
		us=us+1
		print("user score",us)
		print("comp score",cs)
	elif u=="scissor" and c=="rock":
		cs=cs+1	
		print("comp score",cs)
		print("user score",us)
	if us==3:
		print("user wins")
	elif cs==3:
		print("comp wins")