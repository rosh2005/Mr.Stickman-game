import random
num = random.randint(1, 1000)
while True:
	print('Guess a number between 1 and 1000')
	guess = input()
	i = int(guess)
	if i == num:
		print('You Win!')
		break
	elif i < num:
		print('Higher!')
	elif i > num:
		print('Lower!')

		


