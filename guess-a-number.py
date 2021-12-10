import random
def run_guess(guess, answer):
	if 0 < guess < 11:
		if guess==answer:
			print('You\'re a genius')
			return True
	else:
		print('1 to 10 please.')
		return False

if __name__ == '__main__':
	answer = random.randint(1,10)
	while True:
		try:
			guess = int(input('Guess a number between 1~10: '))
			run_guess(guess, answer)
		except ValueError:
			print('Please enter a number.')
			continue
