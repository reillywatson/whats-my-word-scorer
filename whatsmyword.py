import getpass
import random

totalScore = 0
word = getpass.getpass('Enter your word, or enter nothing to take a random word')
if word == '':
	words = open('/usr/share/dict/words').read().split('\n')
	words = [a for a in words if len(a) == 6 or len(a) == 7]
	word = random.sample(words,1)[0]
ranges = [(0,3), (0,4), (1,5), (2,6), (3,7), (2,7), (1,6), (0,5), (0,6), (1,7), (0,7)]
if len(word) == 6:
	ranges = [(0,2), (0,3), (1,4), (2,5), (3,6), (2,6), (1,5), (0,4), (0,5), (1,6), (0,6)]
for r in ranges:
	guessMask = list('*'*len(word))
	for i in range(r[0],r[1]):
		guessMask[i] = '_'
	guess = raw_input(''.join(guessMask) + ' ').strip()
	while len(guess) != r[1] - r[0]:
		print 'word must be %d letters' % (r[1] - r[0])
		guess = raw_input(''.join(guessMask)).strip()
	j = 0
	for i in range(r[0],r[1]):
		guessMask[i] = guess[j]
		j = j + 1
	score = 0
	wordbag = list(word)
	if wordbag == guessMask:
		score = score + 3000
	for i in range(len(guessMask)):
		if guessMask[i] == word[i]:
			score = score + 1000
			wordbag.remove(guessMask[i])
			guessMask[i] = '*'
	for letter in guessMask:
		if letter in wordbag:
			score = score + 250
			wordbag.remove(letter)
	print score
	totalScore += score
print 'game over! total score: %d' % totalScore
print 'word was: ' + word
