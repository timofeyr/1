import random

number_range = []

number_range.append(int(input("Left limit ")))
number_range.append(int(input("Right limit ")))

number = random.randint(number_range[0], number_range[1])

running = 1

while running:
	guess = int(input("Guess the number "))
	if guess == number:
		running = 0
		print("You guessed it " + str(number))