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
    pointValue = next_line(the_file)
        
    explanation = next_line(the_file)

    return category, question, answers, correct, pointValue, explanation 

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
def high_scores(Score):
    PickleFile=open("Challenge3.txt","a")
    print("Great job! You got made a new high score!")
    Name=input("Name: ")
    NewHighScore=(Name, str(Score))
    PickleFile.writelines(NewHighScore)
    PickleFile.close()
            
def main():
    trivia_file = open_file("Challenge2.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, pointValue, explanation = next_block(trivia_file)
    for qquestion in range(5):
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
        category, question, answers, correct, pointValue, explanation = next_block(trivia_file)
    print("That was the last question!")
    print("You're final score is", score)
    high_scores(score)

    trivia_file.close()

    
 
main()  
input("\n\nPress the enter key to exit.")
