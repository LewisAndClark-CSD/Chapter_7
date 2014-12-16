# Trivia Challenge
# Trivia game that reads a plain text file

import sys
import pickle

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
        
    explanation = next_line(the_file)

    pointValue = next_line(the_file)

    return category, question, answers, correct, explanation, pointValue

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation, pointValue = next_block(trivia_file)
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
            score = score + int(pointValue)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation, pointValue = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    return score

def highScore(score):
    try:
        with open("highScores","rb") as highScoresFile:
            highScores = pickle.load(highScoresFile)
    except:
        highScores = []
    name = input("Enter name: ")
    playerScore = (name, score)
    highScores.append(playerScore)
    for i in highScores:
        print("Player:", i[0])
        print("Score:",i[1])
        print("----")
    highScoresFile.close()
    with open("highScores","wb") as highScoresFile:
        pickle.dump(highScores, highScoresFile)
    highScoresFile.close()

############################################

score = main()
if score > 9:
    highScore(score)
else:
    print("You needed to get a minimum score of 10 to enter the high score list!")
input("\n\nPress the enter key to exit.")
