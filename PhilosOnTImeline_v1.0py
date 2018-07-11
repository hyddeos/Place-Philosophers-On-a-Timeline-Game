import random
import copy

filo0 = ["Socrates", -470, "-Some say that i am ugly but they dont know they dont know anything",0]
filo1 = ["Plato", -428,"-One might wounder how this list looks in the world of forms",0]
filo2 = ["Aristotle", -384, "-Use your logic... i mean MY logic to solve this",0]
filo3 = ["Immanuel Kant", 1724, "-Is this a analytic or syntic timeline?",0]
filo4 = ["Sam Harris", 1967, "-Well you cant play it any other way",0]
filo5 = ["Peter Singer", 1946, "-Please do something useful after this game",0]
filo6 = ["Thales", -624, "I was first",0]
filo7 = ["Democritus",-450, "You cant divde me(complety)",0]
filo8 = ["René Descartes",1596,"Im on the timeline therefor im a Philosopher",0]
filo9 = ["Baruch Spinoza", 1632," Doest matter how you place, everything on this list is god anyway",0]
filo10 = ["John Stuart Mill ", 1806,"Hope you placed me where the happiness was maximized",0]
filo11 = ["David Hume", 1711, "Lets wake them up form their dogmatic slumbers", 0]
filo12 = ["Bertrand Russell", 1872, "Good Job, but be careful to place me in any category",0]
filo13 = ["Saint Thomas Aquinas", 1225, "Looks like you have faith in this", 0]
filo14 = ["Karl Popper", 1902, "Should i really be placed here? Can we test it?"]
filo15 = ["Daniel Dennett", 1942, "The processes in you brain seems to work fine, consciously or not",0]
filo15 = ["Gottfried W. Leibniz", 1646, "Wow, this timeline most be the best of all possible worlds",0]

philosophs = [filo0,filo1,filo2,filo3,filo4,filo5,filo6,filo7,filo8,filo9,filo10,]
rand_philo = []
remaining_philos = copy.deepcopy(philosophs)
played_philos = []
points = 1


def points_add():
#adds one point to overall score
    global points
    points += 1

def lines_func():
    print("_________________________________________________________________"),
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/"),
    print("_________________________________________________________________"),

def startgame_func():
#standard GameStart
    #LOOKS and RULES START
    lines_func()
    print("-"*14,"place Philosopher in the right time".title(), "-"*14,)
    lines_func()
    print("-"*48,"game by Eric S".title(),"-")
    lines_func()
    print("-"*29,"rules".upper(),"-"*29)
    print("Place them according from time of birth\n\nThe timeline is like a ladder\nThe futher back in time the lower on the ladder,".title())
    print("follow instruction to see possible inputs\n".title())
    lines_func()
    #LOOKS END

    start = 0
    while start == 0:
        startgame = input("Place The Philosophers On The Timeline, Ready to Start? y/n  ".lower())
        if startgame == 'y' or startgame == 'yes':
            start = 1
            lines_func()
            game() #starts the game
        else:
            print("Ok, Wrong input. go when ready".title())

def get_random_philo():
#Gets 1 randPhilo and removes it from future and adds it to played philos
    rand_philo = random.choice(remaining_philos)
    played_philos.append(rand_philo)
    remaining_philos.remove(rand_philo)
    return rand_philo

def sort_timeline(list):
    #helps the timeline() func to sort the list according to year in played_philos
    return list[1]

def timeline():
    #Prints and update the status on the timeline
    #Everytime called its sorts the timeline according to year and
    #adds a count in timeline value (nr) and removes the one form last time called.
    nr = 0
    print("Points:", points, "of 10")
    print("THE TIMELINE:")
    print("--Present--")
    played_philos.sort(key = sort_timeline, reverse=True)
    for p in played_philos:
        nr += 1
        p.pop()
        p.append(nr)
        print(nr, ":",p[0])
    print("---Past---\n")

def end_game_timeline(failed_philo):
    #This func is called whenever game ends to se stats
    #When gameover or gamewon
    for p in played_philos:
        if failed_philo[1] == p[1]:
            played_philos.remove(p)

    nr = 0
    print("THE TIMELINE OF THIS GAME WAS:")
    print("--Present--")
    played_philos.sort(key = sort_timeline, reverse=True)
    for p in played_philos:
        nr += 1
        p.pop()
        p.append(nr)
        print(nr, ": Born:",p[1], p[0])
    print("---Past---")

def game():
    place = 0
    print("The first Philosopher to appare on the timeline is:".title(), get_random_philo()[0],"\n")
    while points < 10:
        timeline()
        drawn_philo = get_random_philo()
        print("Time to place:".title(),drawn_philo[0]) #remove [0] to see birth year etc
        print("use keys 1 -".title(),len(played_philos),"to choose where")
        place = input("Where to place?:")
        place = int(place)
        print("")

        #IF PLAYER WHAT TO PUT PHIL LAST ON TIMELINE
        if place > len(played_philos)-1:
            lastphilo = played_philos[-2]
            if drawn_philo[1] <= lastphilo[1]:
                print("Correct, Points added |", drawn_philo[0],"-"+drawn_philo[2]+".\n")
                points_add()
            else:
                gameover(drawn_philo)
        #FOR GUESS WITHIN THE TIMELINE
        for p in played_philos:
            #First For/IF checks if phi placed right compared to past
            if place == p[3]:
                if drawn_philo[1] > p[1]:
                    #Secound For/If compare philo place on timeline to present (if not a 1, top of list)
                    if place != 1:
                        for p in played_philos:
                            if place-1 == p[3]:
                                if drawn_philo[1] < p[1]:
                                    pass
                                else:
                                    gameover(drawn_philo)

                    print("Correct, Points added |", drawn_philo[0], drawn_philo[2]+".\n")
                    points_add()
                else:
                    gameover(drawn_philo)
            else:
                pass
    gamewon()

def gameover(failed_philo):
    lines_func()
    print("GAME OVER")
    print("YOU GOT:", points, "POINTS, BETTER LUCK NEXT TIME")
    end_game_timeline(failed_philo)
    print("You failed to place:".title(), failed_philo[0],"who was born:".title(),failed_philo[1])
    lines_func()
    playagain()

def gamewon():
    lines_func()
    print("congratulations\n you made it\n".upper())
    end_game_timeline('No failed philo')
    lines_func()
    playagain()

def resetgame():
    #Resets for next round
    global points
    points = 1

    while played_philos:
        played_philos.pop()

def playagain():
    resetgame()
    lines_func()
    askplay = True
    while askplay:
        ask = input("Do You Want To Reset The Game?: (y/n)".lower())
        if ask == 'yes' or ask == 'y':
            startgame_func()
        elif ask == 'no' or ask == 'n' or ask == 'quit':
            exit()




startgame_func()


