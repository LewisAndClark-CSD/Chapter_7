"""
3. Change the way the high-scores functionality you created in the last challenge is
   implemented. This time, use a plain text file to store the list.
"""
#Challenge 3
#Andrew Hecky
#12/9/2014

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

def highscores(score):
    highscores = []
    load_scores = True

    """Loading Highscore File"""
    highscore_file = open_file("highscores3.txt", "r") #Opening File [Read Mode]
    while load_scores == True:
        score_line = next_line(highscore_file) #Getting Score Line
        if score_line == '': #Break for when no more scores to load
            break
        score_line = score_line.strip() #Stripping Score Line
        score_list = score_line.split(',') #Making Score line into a list
        score_tuple = (str(score_list[0]), int(score_list[1]))
        highscores.append(score_tuple)#adding to highscore list
    highscore_file.close()#Closing File [Read Mode]
    
    highscores = sorted(highscores, key=lambda tup: tup[1], reverse=True) #Sorting Highscores

    """CHECKING TO SEE IF MADE HIGH SCORES"""
    try: #Checking to see if made highscore list
        for i in highscores:
            if int(score) > int(i[1]):
                addscore = True
            else:
                addscore = False
    except UnboundLocalError:
        addscore = True
    if len(highscores) < 5: #Adding score if max score isnt reached
        addscore = True
    if addscore == True: #If made new highscore
        print("\nYou've set a new highscore! ")
        while True:
            username = input("Enter Your Name: ").title() #getting user name
            if username != '' :
                break
        add = (username, int(score)) #Making New Score for List
        highscores.append(add) #Adding New Score to Highscore List
    else:
        print("\nYou did not set a new highscore... :'(")
    highscores = sorted(highscores, key=lambda tup: tup[1], reverse=True) #Sorting Highscores
    if len(highscores) > 5: #Deleting score if list limit (5) is reached
        highscores.pop(5)

    """PRINTING HIGHSCORES"""
    print("\n\nHIGHSCORES:")
    num1 = 0
    for group in highscores:
        num1 += 1
        print("    " + str(num1) + ") " + group[0] + " :  " + str(group[1]))

    """Writing to Highscore File"""
    highscore_file = open_file('highscores3.txt', "w") #Opening File [Write Mode]
    for i in highscores:
        write_name = str(i[0])
        write_score = str(i[1])
        write_line = (write_name +','+write_score+"\n")
        highscore_file.write(write_line)
    return highscore_file
    highscore_file.close() #Closing File [Write Mode]

        
    

    


    
 
main()
highscores(score)
input("\n\nPress the enter key to exit.")
