from random import randint
import sys

def rollOneDice():
	dice = randint(1, 6)
	print("Number: " + str(dice))

def rollTwoDices():
	dice1 = randint(1, 6)
	dice2 = randint(1, 6)
	print("Numbers: " + str(dice1) + " " + str(dice2))

if __name__ == "__main__":
	play = str(input('Wanna roll a dice?\n"yes" or "no"\n'))
	startLoop = True
	while startLoop:
		if play.lower() == "yes":
			startLoop = False
			running = True
			while running:
				ans = int(input('1 or 2 dices?\n'))
				if ans == 1:
					running = False
					rollOneDice()
				elif ans == 2:
					running = False
					rollTwoDices()
				else:
					print("Something went wrong, try again\n")
		elif play.lower() == "no":
			sys.exit("See ya next time")
		else:
			print("Something went wrong, try again\n")
			play = str(input("Wanna roll a dice?\n"))