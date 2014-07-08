import random

#test for chaos prediction


print 'enter any number between 1 and 1000'
userinput = int(raw_input())
numtries = 0
random.seed()
score = 0
rand = 0

while True:
	#computer attempts to get users input with pseudo random number generator. 
	#Number of tries is the score of user.
	rand = random.randint(1,1000)
	if rand == userinput:
		break
	else:
		score += 1
print 'USER SCORE: ' + str(score)
