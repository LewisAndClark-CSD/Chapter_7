# Trivia Challenge
# Trivia game that reads a plain text file

import sys, pickle, shelve

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
    
    addScore = next_line(the_file)
    
    explanation = next_line(the_file) 

    return category, question, answers, correct, addScore, explanation

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
    category, question, answers, correct, addScore, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(addScore)
            
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, addScore, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    
main()

name = input('Enter your name to go on the highscore list: ')
HIGHSCORE = (name, score)

try:
    highscores = pickle.load(open('highscores.txt', 'rb'))
except:
    highscores = []
    
highscores.append(HIGHSCORE)
highscores = sorted(highscores, key=lambda tup: tup[1], reverse=True)
if len(highscores) > 5:
    highscores.pop()
    
pickle.dump(highscores, open('highscores.txt', 'wb'))

print('\nThe Highscores are: ')
for i in highscores:
    num = i[1]
    print(i[0] + ' - ' + str(num))

input("\n\nPress the enter key to exit.")
