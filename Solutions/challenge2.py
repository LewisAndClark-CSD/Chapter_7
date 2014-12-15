"""
2. Improve the Trivia Challenge game so that it maintains a highscores list in a file.
   The program should record the player’s name and score if the player makes the list.
   Store the high scores using a pickled object.
"""
#Challenge 2
#Andrew Hecky
#12/9/2014

# Trivia Challenge
# Trivia game that reads a plain text file

import sys, pickle

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    points = next_line(the_file)
    try:
        points = int(points)
    except ValueError:
        print()
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, points, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    global score
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:
        print()
        # ask a question
        print(category)
        print("This question is worth " + str(points) + " points!\n")
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(points)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

    
 
main()
addscore = True
username = ""
    ###HIGHSCORES###
try:
    highscores = pickle.load(open('highscores.txt', 'rb')) #Loading
except EOFError:
    highscores = []
highscores = sorted(highscores, key=lambda tup: tup[1], reverse=True)
try:
    for i in highscores:
        if score > i[1]:
            addscore = True
        else:
            addscore = False
except UnboundLocalError:
    addscore = True
if len(highscores) < 5:
    addscore = True
if addscore == True:
    print("\nYou've set a new highscore! ")
    while username == "":
        username = input("Enter Your Name: ")
    add = (username, int(score))
    highscores.append(add)
    highscores = sorted(highscores, key=lambda tup: tup[1], reverse=True)
    if len(highscores) > 5:
        highscores.pop(5)
    print("\n    HIGHSCORES:")
    num1 = 0
for i in highscores:
    num1 += 1
    num = i[1]
    print("\t" + str(num1) + ") " + i[0] + ': ' + str(num))
pickle.dump(highscores,open('highscores.txt','wb'))

input("\n\nPress the enter key to exit.")
