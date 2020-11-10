import time 
import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("900x400")

def accuracy(error):
    return round(100 - (error / len(textTesting))*100)

def wpm(totalWords, time):
    speed = totalWords / time * 60
    return round(speed)

def typeTestingGame():
    b1.destroy()
    global entry
    global label
    global listWords
    global textTesting
    global currentChar
    global error 
    global count


    sourceText = {1 : "Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.",
                  2 : "A ferocious serpent that was being hunted by Atlanteans. Battle-weary and ragged, it came upon an ancient light, and gained new strength for its battle. With its increased power, it launched an invasion of enemy territory with a renewed assault.",
                  3 : "In the town where I was born, lived a man who sailed to sea, and he told us of his life, in the land of submarines, so we sailed on to the sun, till we found a sea of green, and we lived beneath the waves, in our yellow submarine.",
                  4 : "The snail drops deep as does my rock. I never nuzzle, cause to nuzzle is the husband of talk. Beyond the walls of flamingos, life is defined. I think of love when I'm in a Russia state of mind.",
                  5 : "The fairy godmother changed a pumpkin into a coach and some mice into footmen. Before Cinderella left, the fairy godmother warned her to be home before midnight, because the spell would only last till then.",
                  6 : "When Snow White took a bite of the apple, she fell down unconscious. The dwarves were very sad and built a glass coffin for her. One day a prince came by and saw how beautiful Snow White was, and bent down to give her a kiss.",
                  7 : "The main difference is that socialism is compatible with democracy and liberty, whereas Communism involves creating an 'equal society' through an authoritarian state, which denies basic liberties.",
                  8 : "Far curiosity incommode now led smallness allowance. Favour bed assure son things yet. She consisted consulted elsewhere happiness disposing household any old the. Widow downs you new shade drift hopes small.",
                  9 : "Resolution possession discovered surrounded advantages has but few add. Yet walls times spoil put. Be it reserved contempt rendered smallest. Studied to passage it mention calling believe an. Get ten horrible remember pleasure two vicinity.",
                  10 : "And if you feel you're sinking, I will jump right over into cold, cold water for you. And although time may take us into different places, I will still be patient with you. And I hope you know",
              }
    textTesting = sourceText[random.randint(1,10)]

    global listWords
    global totalWords
    listWords = textTesting.split(" ")
    totalWords = len(listWords)

    global x2
    x2 = Text(window, font = "times 20", width = 35, height = 8, wrap = WORD)
    x2.insert(END, textTesting)
    x2.pack(side = TOP)

    x3 = Label(window, text = "Start typing: ", font = "times 20")
    x3.place(x = 10, y = 50)

    countDown = 10
    x4 = Label(window, text = countDown, font = "times 20")
    x4.place(x = 150, y = 50)
    window.update()
    for i in range(0, 10):
        time.sleep(1)
        countDown -= 1
        x4.config(text = countDown)
        window.update()
    global startTime
    if countDown == 0:
        startTime = time.time()    

    entry = Entry(window, width = 25, font = "times 20")
    entry.place(x = 280, y = 280, height = 40)
    entry.pack(side = TOP)

    global changedRed
    changedRed = False
    global count
    count = 0
    global currentIndex 
    currentIndex = 0

    entry.bind_all("<KeyPress>", checkError)
    window.update()

def deleteEntry(e):
    global entry
    entry.delete(0, END)

def checkError(e): 
    global error 
    global startTime
    global changedRed
    global listWords
    global count
    global x2
    global currentIndex 

    currentChar = entry.get()
    currentWord = listWords[count]

    x2.tag_add('underline', "1." + str(currentIndex),"1." + str(currentIndex + len(currentWord)))
    x2.tag_config('underline', font = "times 20 underline")
    x2.tag_add('currentCharWrong', '1.' + str(currentIndex + len(currentChar) - 1), '1.' + str(currentIndex + len(currentChar)))
    if count >= 1:
        x2.tag_add('finish', '1.0', '1.' + str(currentIndex - 1))
        x2.tag_config('finish', font = 'times 20', background = 'white', foreground = 'green')
    window.update()
    
    if currentChar != "":
        if currentChar != currentWord[:len(currentChar)]:
            x2.tag_config('currentCharWrong', font = "times 20 underline", background = "red")
            if changedRed == False:
                entry.config({"background" : "red"})
                error += 1
                changedRed = True
        else:
            entry.config({"background" : "white"})
            x2.tag_config('currentCharWrong', font = "times 20 underline", background = "yellow")
            changedRed = False
        if currentChar == currentWord:
            entry.config({"background" : "white"})
            count += 1
            entry.bind_all("<space>", deleteEntry)
            currentIndex = currentIndex + len(currentWord) + 1
            x2.tag_config('underline', font = "times 20 underline")
            x2.tag_config('green', foreground = 'green', font = "times 20")
            window.update()

    if currentChar == listWords[-1]:
        endTime = time.time()
        timeTol = round(endTime - startTime)
        totalTime = "Total time taken: {}s".format(timeTol)
        wordPerMin = "wpm: " + str(wpm(totalWords, timeTol))
        errors = "Number of errors: " + str(error)
        acc = "Accuracy: {}%".format(accuracy(error))
        messagebox.showinfo('Result', totalTime + '\n' + wordPerMin + '\n' + errors + '\n' + acc)

error = 0
x1 = Label(window, text = "Typing test", font = "times 20")
x1.place(x = 10, y = 50)
b1 = Button(window, text = "Start", command = typeTestingGame, width = 10, bg = 'grey', font = "times 20")
b1.place(x = 150, y = 100, height = 40)
window.mainloop()
