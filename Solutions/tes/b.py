import pickle, sys
highscores = []
name = "Andrew"
score = 4

try:
    with open('b.txt', 'rb') as input:
        highscores = pickle.load(input)
    print(highscores)
except EOFError:
    print("Error")
"""
highscore = (name, str(score))
with open('b.txt', 'wb') as output:
    highscore1 = (name, score)
    pickle.dump(highscore1, output)
print(highscore1)
with open('b.txt', 'rb') as input:
    highscore1 = pickle.load(input)
print(highscore1)
"""

add = [name, score]
add.append(highscores)
numofScores = 0
for i in highscores:
    numofScores += 1
if numofScores > 5:
    try:
        highscores.remove(6)
    except ValueError:
        print(" ", end="")
        
print(highscores)

with open('b.txt', 'wb') as output:
    pickle.dump(highscores, output)
print(highscores)

with open('b.txt', 'rb') as input:
    highscores = pickle.load(input)

print(highscores)
