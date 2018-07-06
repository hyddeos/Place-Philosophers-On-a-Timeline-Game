import random
import numpy
import copy

filo0 = ["Socrates", -470, "-Some say that i am ugly but they dont know they dont know anything"]
filo1 = ["Plato", -428,"-One might wounder how this list looks in the world of forms"]
filo2 = ["Aristotle", -384, "-Use your logic... i mean MY logic to solve this"]
filo3 = ["Immanuel Kant", 1724, "-Is this a analytic or syntic timeline?"]
filo4 = ["Sam Harris", 1967, "-Well you cant play it any other way"]
filo5 = ["Peter Singer", 1946, "-Please do something useful after this game"]
filo6 = ["Thales", -624, "I was first"]
filo7 = ["Democritus",-450, "You cant divde me(complety)"]
filo8 = ["René Descartes",1596,"Im on the timeline therefor im a Philosopher"]
filo9 = ["Baruch Spinoza", 1632," Doest matter how you place, everything on this list is god anyway"]
filo10 = ["John Stuart Mill ", 1806,"Hope you placed me where the happiness was maximized"]


filosofer = [filo0,filo1,filo2,filo3,filo4,filo5,filo6,filo7,filo8,filo9,filo10,]
slumpadfilosof = []
filosoferhog = copy.deepcopy(filosofer)
filosoferlagda = []

cards = 0


def lines_func():
#ritar lite
    print("_________________________________________________________________"),
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/"),
    print("_________________________________________________________________"),
    

def startgame_func():
#standard GameStart
    lines_func()
    print("-"*14,"place Philosopher in the right time".title(), "-"*14,)
    lines_func()
    start = 0
    print("-"*48,"game by Eric S".title(),"-")
    lines_func()

    while start == 0:
        startgame = input("Place the Philosophers on the timeline, Ready to Start? y/n  ")
        if startgame == 'y' or startgame == 'yes':
            start = 1
            addcard_func(cards)
            lines_func()
            print("The first Philosopher to appare on the timeline is:", slumpadfilosof_func()[0])
            lines_func()
        else:
            print("Ok, Wrong input. to when ready")

      
def slumpadfilosof_func():
#Slumpar filosof, lägger till filosof i filosoferlagda och tar bort ur hög, filosoferhog
    slumpadfilosof = random.choice(filosoferhog)
    filosoferlagda.append(slumpadfilosof)
    filosoferhog.remove(slumpadfilosof)
    return slumpadfilosof[0:3]


def listalagda_func():
#Listar ut endast namnet på de utladga filosoferna
    count = 1
    templista = sorted(filosoferlagda, key=lambda x: x[1])
    print("-----TIMELINE and points:", cards, "of 10" )
    for i in range(len(filosoferlagda)):
        print(count,":", templista[i][0:2])
        count += 1
    lines_func()
        

        
def question_func():
#kollar om svaret är rätt eller fel
    filo = slumpadfilosof_func()
    print("Next Philosopher to Place:", filo[0])
    for i in range(cards):
        print("Was", filo[0], "born before", filosoferlagda[i][0],"?")
        answer = input("yes or no (y/n)")
        if answer == 'yes' or answer == 'y':
                if filo[1] < (filosoferlagda[i][1]):
                    print ("Correct")
                    
                    

                else:
                    wrong_func()      
        else:
                if filo[1] > (filosoferlagda[i][1]):
                    print("Correct")
                    
                else:
                    wrong_func()
           
           

    

def addcard_func(x):
    global cards
    cards += 1
    return cards

def wrong_func():
#funktionen anropas när man gissar fel och frågar om man vill spela igen
    print ("Wrong, Game over! You got ", cards, "Points")
    print("felsökning", filosoferlagda, "1", slumpadfilosof )
    quit()
    """rematch = input("Yes or no: ")
    if rematch == 'yes' or rematch == 'y':
        startgame_func()"""

startgame_func()
while cards != 10:
    question_func()
    addcard_func(cards)
    listalagda_func()
else:
    print("You WON THE GAME")



