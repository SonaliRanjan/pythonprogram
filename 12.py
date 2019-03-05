import random
l=["rock","paper","scissor"]
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
		print("comp wins")
	elif  u=="rock" and c=="scissor":
		print("user wins")
	elif u=="paper" and c=="rock":
		print("user wins")
	elif u=="paper" and c =="scissor":
		print("comp wins")
	elif u=="scissor" and c=="paper":
		print("user wins")
	elif u=="scissor" and c=="rock":