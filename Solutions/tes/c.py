import pickle

#Making highscores list
highscores = [('Andrew', int(4)), ('Brad', int(3)), ("Nathan", int(6)), ('Bo', int(2))]
print('1', highscores)

#Saving highscores list
def savescore(highscores):
    pickle.dump(highscores,open('c.txt', 'wb'))
    print('2', highscores)
    return highscores

#Clearing highscores list
def clearscore(highscores):
    highscores = []
    print('3', highscores)
    return highscores

#Reading highscores list
def loadscore(highscores):
    highscores = pickle.load(open('c.txt', 'rb'))
    print('4', highscores)
    return highscores

#Printing highscores list
def printscore(highscores):
    for name in highscores:
        print(name[0] + ':' + str(name[1]))

#Sorting highscores list
def sortscore():
    global highscores
    highscores = sorted(highscores, key=lambda score: score[1], reverse=True)
    return highscores


def main():
    score = 3
    savescore(highscores)
    clearscore(highscores)
    loadscore(highscores)
    printscore(highscores)
    sortscore()
    printscore(highscores)
    for i in highscores:
        if score > i[1] :
            print("You've set a high score!")
        else:
            print("Nope")

main()
    
