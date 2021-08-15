from tkinter import *
import os
import random
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
import sys

pygame.mixer.init()
music = pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), r"DefaultMusic.mp3"))
pygame.mixer.music.play(-1)
click = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), r"Click.ogg"))
ding = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), r"Ding.ogg"))
sadness = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), r"sadness.ogg"))
"""
questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "The ipad is manufactured by?",
             "Who founded Microsoft?", 'Which vegetable gives Popeye his strength?', 'Who was the ancient Greek goddess of love and beauty?', 'Which alcoholic drink is made from the leaves of the agave plant and gets its name from an area around a Mexican city?', 'What does the Q in IQ stand for?', 'According to legend, kissing which stone in Ireland gives you the gift of the gab?', 'In which US city is NASA’s Mission Control Center located?', 'What is the Latin word for “beyond”, often used as a prefix to signify an extreme?', 'Bronze is mainly an alloy of tin and which other metal?', 'In meteorology, what name is given to a line of equal pressure on a map?', 'Formentera is part of which group of Spanish islands?', 'In which US national park is the Old Faithful geyser found?', 'Casablanca is the largest city in which African country?', 'What is the largest freshwater lake in the world by surface area?', 'Toronto is the capital city of which Canadian province?', 'The architect IM Pei designed a glass and steel pyramid for which capital city?', 'Which Spanish city is famous for its ‘running of the bull’ during the annual San Fermin festival?', 'What is the national flower of Scotland?', 'Manitoulin Island is the world’s largest island in a lake In which of the Great Lakes of North America is it found?', 'What is the capital city of Ukraine?', 'What was the name of the ship in which Captain James Cook made his first expedition to the Pacific Ocean?', 'Which naval battle between the British fleet and the combined French and Spanish fleets took place on the 21st October, 1805?', 'Napoloen Bonaparte escaped from his exile on which Mediterranean island in February, 1815?', 'Operation Overlord took place on the beaches of which region of France in June, 1944?', 'Which US president said, “government of the people, by the people, for the people” in his Gettysburg Address?', 'Who was Roman emperor at the time of Christ’s crucifixion?', 'In what year did the Bay of Pigs invasion take place?', 'What was the name of the first spacecraft to land on the moon?', 'Where was the second atomic bomb dropped in World War 2?', 'Which US president abolished slavery?', 'What nationality was the artist Rembrandt?', 'Who created and wrote about the fictional continent Middle Earth?', 'How was American writer Samuel Langhorne Clemens better known?', 'Which artist’s works include “The Persistence of Memory”, “The Temptation of St Anthony”, and “Lobster Telephone”?', 'In which novel are Ralph, Jack and Peterkin three castaways?', 'Which classic science fiction novel begins with the line, “Behind every man now alive stand thirty ghosts, for that is the ratio by which the dead outnumber the living”?', 'Pablo Picasso and George Braques were pioneers of which early nineteenth century art movement noted for it’s concentration on geometrical figures?', 'Which novel begins with the line, “It was a bright cold day in April, and the clocks were striking thirteen”?']

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz", 'Broccoli', 'Aphrodite', 'Tequila', 'Quantity', 'The Blarney Stone', 'Huntsville, Alabama', 'Extra', 'Brass', 'Isotherm', 'Canary Islands', 'Yellowstone', 'Egypt', 'Lake Superior', 'Alberta', 'London', 'Barcelona', 'Heather', 'Lake Huron', 'Kiev', 'Beagle', 'Battle of Waterloo', 'Corsica', 'Provence', 'Abraham Lincoln', 'Nero', '1959', 'Spider', 'Nagasaki', 'Thomas Jefferson', 'German', 'Terry Pratchett', 'Mark Twain', 'Picasso', 'Treasure Island', '2001 – A Space Odyssey', 'Impressionism', '1984']

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio",'Spinach', 'Calliope', 'Singani', 'Quorum', 'The Baloney Stone', 'Houston, Texas', 'Super', 'Lead', 'Isobar', 'Cies Islands', 'Death Valley', 'Morocco', 'Lake Victoria', 'Quebec', 'Paris', 'Seville', 'Gorse', 'Lake Michigan', 'Vilnius', 'Endeavour', 'Battle of Trafalgar', 'Capri', 'Aquitaine', 'George Washington', 'Pontius Pilate', '1961', 'Eagle', 'Hiroshima', 'James Garfield', 'Belgian', 'J R R Tolkien', 'Walt Whitman', 'Salvador Dali', 'Lord of the Flies', 'The Time Machine', 'Realism', 'David Copperfield']
third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates",'Asparagus', 'Athena', 'Chicha', 'Quality', 'The Rosetta Stone', 'Hampton, Virginia', 'Ultra', 'Iron', 'Isochor', 'Medes Islands', 'Yosemite', 'Tunisia', 'Lake Tanganyika', 'British Columbia', 'Beijing', 'Pamplona', 'Bluebell', 'Lake Erie', 'Minsk', 'Bounty', 'Battle of Jutland', 'Sicily', 'Burgundy', 'Thomas Jefferson', 'Tiberius', '1963', 'Intrepid', 'Osaka', 'Abraham Lincoln', 'Swiss', 'George R R Martin', 'Joseph Heller', 'Jackson Pollock', 'The Coral Island', 'Dune', 'Cubism', 'The Great Gatsby']

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos",'Lentils', 'Calypso', 'Kasiri', 'Quotient', 'The Stone of Destiny', 'Cape Canaveral, Florida', 'Mega', 'Copper', 'Isoquant', 'Balearic Islands', 'Carlsbad Caverns', 'Algeria', 'Lake Baikal', 'Ontario', 'Toky', 'Tarragona', 'Thistle', 'Lake Ontario', 'Pristina', 'Endurance', 'Battle of the Nile', 'Elba', 'Normandy', 'James Buchanan', 'Julius Caesar', '1965', 'Falcon', 'Yokohama', 'Andrew Johnson', 'Dutch', 'Neil Gaiman', 'John Steinbeck', 'Rene Magritte', 'Robinson Crusoe', 'The Martian Chronicles', 'Abstract Expressionism', 'Ulysses']

correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "7:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates",'Spinach', 'Aphrodite', 'Tequila', 'Quotient', 'Krypton', 'The Blarney Stone', 'Houston, Texas', 'Ultra', 'Copper', 'Isobar', 'Balearic Islands', 'Yellowstone', 'Morocco', 'Lake Superior', 'Ontario', 'Paris', 'Pamplona', 'Thistle', 'Lake Huron', 'Kiev', 'Endeavour', 'Battle of Trafalgar', 'Elba', 'Normandy', 'Abraham Lincoln', 'Tiberius', '1961', 'Eagle', 'Nagasaki', 'Abraham Lincoln', 'Dutch', 'J. R. R. Tolkien', 'Mark Twain', 'Salvador Dali', 'The Coral Island', '2001 – A Space Odyssey', 'Cubism', '1984', 'Michelangelo']
"""

questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "The ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]
                

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio",]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "7:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]

d = []
for num in range(len(questions)):
    d.append([questions[num], first_option[num], second_option[num], third_option[num], fourth_option[num], correct_answers[num]])
random.shuffle(d)
questions = []

first_option = []

second_option = []

third_option = []

fourth_option = []

correct_answers = []
for x in d:
    questions.append(x[0])
    first_option.append(x[1])
    second_option.append(x[2])
    third_option.append(x[3])
    fourth_option.append(x[4])
    correct_answers.append(x[5])

currentQuestion = 0
root = Tk()

root.geometry('1270x652+0+0')
root.title("Who wants to be a millionare?")

root.config(bg="black")





picture0 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture0.png'))
picture1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture1.png'))
picture2 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture2.png'))
picture3 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture3.png'))
picture4 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture4.png'))
picture5 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture5.png'))
picture6 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture6.png'))
picture7 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture7.png'))
picture8 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture8.png'))
picture9 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture9.png'))
picture10 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture10.png'))
picture11 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture11.png'))
picture12 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture12.png'))
picture13 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture13.png'))
picture14 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture14.png'))
picture15 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture15.png'))

images = [picture1, picture2, picture3, picture4, picture5, picture6, picture7, picture8, picture9, picture10, picture11, picture12, picture13, picture14, picture15]

moneyAmounts = [[0, 'Better luck next time...'], [100, 'Better luck next time...'], [200, 'Better luck next time...'], [300, 'That\'s ok, I guess...'], [400, 'That\'s ok, I guess...'], [500, 'That\'s ok, I guess...'], [1000, 'That\'s ok, I guess...'], [2000, 'Nice!'], [4000, 'Nice!'], [8000, 'Nice!'], [16000, 'Nice!'], [32000, 'Nice!'], [64000, 'Great Job!'], [125000, 'Great Job!'], [250000, 'Great Job!'], [500000, 'Very Nice!'], [1000000, 'WOW!!!']]
leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)

topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid(row=0, column=0)

centerFrame = Frame(leftFrame, bg='black', pady=15)
centerFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black')
bottomFrame.grid(row=2, column=0)

rightFrame = Frame(root, bg='black')
rightFrame.grid(row=0, column=1, pady=25, padx=50)

image50 = PhotoImage(file=os.path.join(os.path.dirname(__file__), '50-50.png'))
image50X = PhotoImage(file=os.path.join(os.path.dirname(__file__), '50-50-X.png'))
lifeline50Button = Button(topFrame, image=image50, bg='black', bd=0, activebackground='black', width=180, height=80, cursor='hand2')
lifeline50Button.grid(row=0,column=0)

audiencePoll = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'audiencePole.png'))
audiencePollX = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'audiencePoleX.png'))
audiencePollButton = Button(topFrame, image=audiencePoll, bg='black', bd=0, activebackground='black', width=180, height=80, cursor='hand2')
audiencePollButton.grid(row=0,column=1)

phoneAFriend = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'phoneAFriend.png'))
phoneAFriendX = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'phoneAFriendX.png'))
phoneAFriendButton = Button(topFrame, image=phoneAFriend, bg='black', bd=0, activebackground='black', width=180, height=80, cursor='hand2')
phoneAFriendButton.grid(row=0,column=2)

centerImage = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'center.png'))
logoLabel = Label(centerFrame, image=centerImage, bg='black', bd=0, width=300, height=200)
logoLabel.grid(row=0, column=0)

amountImage = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Picture0.png'))
amountLabel = Label(rightFrame, image=amountImage, bg='black')
amountLabel.grid(row=0, column=0)

layoutImage = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'lay.png'))
layoutLabel = Label(bottomFrame, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0)

questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), bg='black', fg='white', width=34, height=2, wrap='word', bd=0)
questionArea.place(x=70, y=10)

questionArea.insert(END, questions[0])

labelA=Label(bottomFrame, font=('arial', 18, 'bold'), text='A:', bg='black', fg='white')
labelA.place(x=60, y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', cursor='hand2',bd=0, activebackground='black', activeforeground='white')
optionButton1.place(x=100, y=100)


labelB=Label(bottomFrame, font=('arial', 18, 'bold'), text='B:', bg='black', fg='white')
labelB.place(x=330, y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', cursor='hand2',bd=0, activebackground='black', activeforeground='white')
optionButton2.place(x=370, y=100)


labelC=Label(bottomFrame, font=('arial', 18, 'bold'), text='C:', bg='black', fg='white')
labelC.place(x=60, y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', cursor='hand2',bd=0, activebackground='black', activeforeground='white')
optionButton3.place(x=100, y=180)


labelD=Label(bottomFrame, font=('arial', 18, 'bold'), text='D:', bg='black', fg='white')
labelD.place(x=330, y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', cursor='hand2',bd=0, activebackground='black', activeforeground='white')
optionButton4.place(x=370, y=180)
def select(event):
    global currentQuestion
    global amountLabel
    global labelA, labelB, labelC, labelD
    v = False
    pygame.mixer.Sound.play(click)
    options = [optionButton1, optionButton2, optionButton3, optionButton4]
    otherOptions=[optionButton1, optionButton2, optionButton3, optionButton4]
    labels = [labelA, labelB, labelC, labelD]
    correctOption = ''
    def waithere(time):
        var = IntVar()
        root.after(time, var.set, 1)
        root.wait_variable(var)
    if first_option[currentQuestion] in correct_answers:
        correctOption = optionButton1
        options.remove(optionButton1)
    elif second_option[currentQuestion] in correct_answers:
        correctOption = optionButton2
        options.remove(optionButton2)
    elif third_option[currentQuestion] in correct_answers:
        correctOption = optionButton3
        options.remove(optionButton3)
    elif fourth_option[currentQuestion] in correct_answers:
        correctOption = optionButton4
        options.remove(optionButton4)
    correctOption['foreground'] = 'green'
    labels[otherOptions.index(correctOption)]['foreground'] = 'green'
    for item in options:
        item['foreground'] = 'red'
        labels[otherOptions.index(item)]['foreground'] = 'red'
    waithere(2000)
    correctOption['foreground'] = 'white'
    labels[otherOptions.index(correctOption)]['foreground'] = 'white'
    for item in options:
        item['foreground'] = 'white'
        labels[otherOptions.index(item)]['foreground'] = 'white'
        
    try:
        value = event.widget['text']
        if correct_answers[currentQuestion] in value:
            pygame.mixer.Sound.play(ding)
            currentQuestion += 1
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[currentQuestion])
            
            optionButton1.config(text=first_option[currentQuestion])
            optionButton2.config(text=second_option[currentQuestion])
            optionButton3.config(text=third_option[currentQuestion])
            optionButton4.config(text=fourth_option[currentQuestion])
            amountLabel.config(image=images[currentQuestion])
        else:
            topFrame.destroy()
            centerFrame.destroy()
            bottomFrame.destroy()
            #rightFrame.destroy()
            labelA=Label(leftFrame, font=('arial', 30, 'bold'), text=f'You won ${moneyAmounts[currentQuestion][0]}! {moneyAmounts[currentQuestion][1]}', bg='black', fg='white')
            labelA.place(relx=0.5, rely=0.5, anchor=CENTER)
            if currentQuestion >= 10:
                win = pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), r"Win.ogg"))
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.Sound.play(sadness)
            waithere(35000)
            v = True
    except:
        if v:
            pygame.quit()
            sys.exit()
            quit()
        win = pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), r"Win.ogg"))
        pygame.mixer.music.play(-1)
        topFrame.destroy()
        centerFrame.destroy()
        bottomFrame.destroy()
        #rightFrame.destroy()
        labelA=Label(leftFrame, font=('arial', 30, 'bold'), text=f'You won $1000000! WOW!', bg='black', fg='white')
        labelA.place(relx=0.5, rely=0.5, anchor=CENTER)
        waithere(35000)
        pygame.quit()
        sys.exit()
        quit()
    
def removeWrongAnswers(type):
    global currentQuestion
    options = [(optionButton1, first_option[currentQuestion]), (optionButton2, second_option[currentQuestion]), (optionButton3, third_option[currentQuestion]), (optionButton4, fourth_option[currentQuestion])]
    if first_option[currentQuestion] in correct_answers:
        options.remove((optionButton1, first_option[currentQuestion]))
    elif second_option[currentQuestion] in correct_answers:
        options.remove((optionButton2, second_option[currentQuestion]))
    elif third_option[currentQuestion] in correct_answers:
        options.remove((optionButton3, third_option[currentQuestion]))
    elif fourth_option[currentQuestion] in correct_answers:
        options.remove((optionButton4, fourth_option[currentQuestion]))
    del options[random.choice([0, 1, 2])]
    for option in options:
        option[0].config(text='NOT IT')
    lifeline50Button.unbind('<Button-1>')
    lifeline50Button['state']=DISABLED
    lifeline50Button['cursor']='arrow'

def phoneAFriendf(type):
    """global currentQuestion
    options = [(optionButton1, first_option[currentQuestion]), (optionButton2, second_option[currentQuestion]), (optionButton3, third_option[currentQuestion]), (optionButton4, fourth_option[currentQuestion])]
    correct = random.choice([True, True, True, True, True, True, True, True, True, False])
    if correct:
        if first_option[currentQuestion] in correct_answers:
            options.remove((optionButton1, first_option[currentQuestion]))
        elif second_option[currentQuestion] in correct_answers:
            options.remove((optionButton2, second_option[currentQuestion]))
        elif third_option[currentQuestion] in correct_answers:
            options.remove((optionButton3, third_option[currentQuestion]))
        elif fourth_option[currentQuestion] in correct_answers:
            options.remove((optionButton4, fourth_option[currentQuestion]))
    else:
        del options[random.choice([0, 1, 2, 3])]
    for option in options:
        option[0].config(text='NOT IT')
    phoneAFriendButton.unbind('<Button-1>')
    phoneAFriendButton['state']=DISABLED
    phoneAFriendButton['cursor']='arrow'"""
    global currentQuestion
    options = [(optionButton1, first_option[currentQuestion]), (optionButton2, second_option[currentQuestion]), (optionButton3, third_option[currentQuestion]), (optionButton4, fourth_option[currentQuestion])]

    if first_option[currentQuestion] in correct_answers:
        options.remove((optionButton1, first_option[currentQuestion]))
    elif second_option[currentQuestion] in correct_answers:
        options.remove((optionButton2, second_option[currentQuestion]))
    elif third_option[currentQuestion] in correct_answers:
        options.remove((optionButton3, third_option[currentQuestion]))
    elif fourth_option[currentQuestion] in correct_answers:
        options.remove((optionButton4, fourth_option[currentQuestion]))

    for option in options:
        option[0].config(text='NOT IT')
    phoneAFriendButton.unbind('<Button-1>')
    phoneAFriendButton['state']=DISABLED
    phoneAFriendButton['cursor']='arrow'
    

def audiencePollf(type):
    global currentQuestion
    options = [[optionButton1, first_option[currentQuestion]], [optionButton2, second_option[currentQuestion]], [optionButton3, third_option[currentQuestion]], [optionButton4, fourth_option[currentQuestion]]]


    def findRandomPercents():
        while True:
            percentOne = random.randint(0, 90)
            try:
                percentTwo = random.randint(0, percentOne-10)
            except:
                percentTwo = random.randint(0, -(percentOne-10))
            try:
                percentThree = random.randint(0, percentTwo-10)
            except:
                percentThree = random.randint(0, -(percentTwo-10))
            percentFour = 100-(percentOne+percentTwo+percentThree)
            if percentFour > 0:
                break
        x = [percentOne, percentTwo, percentThree, percentFour]
        x.sort(reverse=True)
        return x



    percents = findRandomPercents()
    if first_option[currentQuestion] in correct_answers:
        options[0].append(percents[0])
        options[1].append(percents[1])
        options[2].append(percents[2])
        options[3].append(percents[3])
    elif second_option[currentQuestion] in correct_answers:
        options[0].append(percents[1])
        options[1].append(percents[0])
        options[2].append(percents[2])
        options[3].append(percents[3])
    elif third_option[currentQuestion] in correct_answers:
        options[0].append(percents[2])
        options[1].append(percents[1])
        options[2].append(percents[0])
        options[3].append(percents[3])
    elif fourth_option[currentQuestion] in correct_answers:
        options[0].append(percents[3])
        options[1].append(percents[1])
        options[2].append(percents[2])
        options[3].append(percents[0])

    for option in options:
        option[0].config(text=option[1]+" "+str(option[2])+"%")
    audiencePollButton.unbind('<Button-1>')
    audiencePollButton['state']=DISABLED
    audiencePollButton['cursor']='arrow'

def on_leave1(event):
    if optionButton1['fg'] == 'grey':
        optionButton1['fg'] = 'white'
        labelA['fg'] = 'white'
 
def on_enter1(event):
    if optionButton1['fg'] == 'white':
        optionButton1['fg'] = 'grey'
        labelA['fg'] = 'grey'

def on_leave2(event):
    if optionButton2['fg'] == 'grey':
        optionButton2['fg'] = 'white'
        labelB['fg'] = 'white'
 
def on_enter2(event):
    if optionButton2['fg'] == 'white':
        optionButton2['fg'] = 'grey'
        labelB['fg'] = 'grey'

def on_leave3(event):
    if optionButton3['fg'] == 'grey':
        optionButton3['fg'] = 'white'
        labelC['fg'] = 'white'
 
def on_enter3(event):
    if optionButton3['fg'] == 'white':
        optionButton3['fg'] = 'grey'
        labelC['fg'] = 'grey'

def on_leave4(event):
    if optionButton4['fg'] == 'grey':
        optionButton4['fg'] = 'white'
        labelD['fg'] = 'white'
 
def on_enter4(event):
    if optionButton4['fg'] == 'white':
        optionButton4['fg'] = 'grey'
        labelD['fg'] = 'grey'

def on_leavelifeline(event):
    if lifeline50Button["state"] == "normal":
        lifeline50Button['image'] = image50
 
def on_enterlifeline(event):
    if lifeline50Button["state"] == "normal":
        lifeline50Button['image'] = image50X

def on_leavePoll(event):
    if audiencePollButton["state"] == "normal":
        audiencePollButton['image'] = audiencePoll
 
def on_enterPoll(event):
    if audiencePollButton["state"] == "normal":
        audiencePollButton['image'] = audiencePollX

def on_leavePhone(event):
    if phoneAFriendButton["state"] == "normal":
        phoneAFriendButton['image'] = phoneAFriend
 
def on_enterPhone(event):
    if phoneAFriendButton["state"] == "normal":
        phoneAFriendButton['image'] = phoneAFriendX

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

optionButton1.bind('<Leave>', on_leave1)
optionButton1.bind('<Enter>', on_enter1)

optionButton2.bind('<Leave>', on_leave2)
optionButton2.bind('<Enter>', on_enter2)

optionButton3.bind('<Leave>', on_leave3)
optionButton3.bind('<Enter>', on_enter3)

optionButton4.bind('<Leave>', on_leave4)
optionButton4.bind('<Enter>', on_enter4)


lifeline50Button.bind('<Button-1>', removeWrongAnswers)
audiencePollButton.bind('<Button-1>', audiencePollf)
phoneAFriendButton.bind('<Button-1>', phoneAFriendf)

lifeline50Button.bind('<Leave>', on_leavelifeline)
lifeline50Button.bind('<Enter>', on_enterlifeline)

audiencePollButton.bind('<Leave>', on_leavePoll)
audiencePollButton.bind('<Enter>', on_enterPoll)

phoneAFriendButton.bind('<Leave>', on_leavePhone)
phoneAFriendButton.bind('<Enter>', on_enterPhone)

root.mainloop()
