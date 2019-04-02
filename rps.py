import json
import random
import math
import time

from enum import Enum
from chain import Chain
from rpsenum import movesenum
from datetime import datetime

class RPS:

    def __init__(self, name='allpeople'):
        self.__chainlist = list()
        if name != 'allpeople' and name != "":
            self.__chainlist.append(Chain(name))
        self.__chainlist.append(Chain())
        self.__computer_wins = 0
        self.__user_wins = 0
        self.__draws = 0
        self.__computer_streak = 0
        self.__user_streak = 0

    def resetstats(self):
        self.__computer_wins = 0
        self.__user_wins = 0
        self.__draws = 0
        self.__computer_streak = 0
        self.__user_streak = 0

    def getnextmove(self):


        predictedmoves, reliability = self.__chainlist[0].getpredictedmove()
        if len(self.__chainlist) == 2:
            predictedmoves2, reliability2 = self.__chainlist[1].getpredictedmove()
            purityfactor1 = 0.2*reliability**2
            purityfactor2 = reliability2
            if purityfactor1 < purityfactor2:
                predictedmoves = predictedmoves2 

        if len(predictedmoves) > 3:
            print("something went terribly wrong")
            exit(1)
        elif len(predictedmoves) == 3:
            #We have a random choice here!
            random.seed(datetime.now().microsecond % 10000)
            randnum = random.randint(0,2)
            if randnum == 0:
                return movesenum.rock
            if randnum == 1:
                return movesenum.scissors
            if randnum == 2:
                return movesenum.paper
        elif len(predictedmoves) == 2:
            if movesenum.scissors in predictedmoves and movesenum.paper in predictedmoves:
                return movesenum.scissors
            elif movesenum.rock in predictedmoves and movesenum.scissors in predictedmoves:
                return movesenum.rock
            elif movesenum.rock in predictedmoves and movesenum.paper in predictedmoves:
                return movesenum.paper
        elif len(predictedmoves) == 1:
            if movesenum.scissors in predictedmoves:
                return movesenum.rock
            if movesenum.paper in predictedmoves:
                return movesenum.scissors
            if movesenum.rock in predictedmoves:
                return movesenum.paper
        elif len(predictedmoves) < 1:
            print("Something went wrong here.")
            exit(1)

    def makemove(self, move):
        if isinstance(move, int):
            move = movesenum(move)
        elif isinstance(move, str):
            move = movesenum[move.lower()]
        elif not isinstance(move, Enum):
            raise TypeError("The parameter move is not a string, an int, or an enum.\nIt is an instance of " + str(type(move)))
        
        for i in self.__chainlist:
            i.makemove(move)

    def quit(self):
        totalgames = self.__computer_wins + self.__user_wins + self.__draws
        for i in self.__chainlist:
            i.savefile()
        print("You won", self.__user_wins, "games.")
        print("And I won", self.__computer_wins, "games.")
        print("We tied", self.__draws, "games\n")
        print("\nThat means that in total I lost {} out of {} times, making my losing rate {:4.2}".format(self.__user_wins, totalgames, self.__user_wins/totalgames))
        print("And you lost {} out of {} times, making your losing rate {:4.2}".format(self.__computer_wins, totalgames, self.__computer_wins/totalgames))
        print("We ended up having a draw {} times, making that be a draw rate of {:4.2}".format(self.__draws, self.__draws/totalgames))

    def evalWinner(self, user_move, computer_move):
        if isinstance(user_move, str):
            user_move = movesenum[user_move]
        
        if user_move.value == computer_move.value:
            print("We're pretty even there!")
            self.__draws += 1
            self.__computer_streak = 0
            self.__user_streak = 0
        elif user_move == movesenum.scissors and computer_move == movesenum.rock:
            print("Yes! I won!!!")
            self.__computer_wins += 1
            self.__computer_streak += 1
            self.__user_streak = 0
            if self.__computer_streak > 2:
                print("I beat you {} times already".format(self.__computer_streak))
        elif user_move.value > computer_move.value or (user_move == movesenum.rock and computer_move == movesenum.scissors):
            print("Dang it! You beat me this time!")
            self.__user_wins += 1
            self.__user_streak += 1
            self.__computer_streak = 0
            if self.__user_streak > 2:
                print("You beat me {} times already".format(self.__user_streak))
        else:
            print("Yes! I won!!!")
            self.__computer_wins += 1
            self.__computer_streak += 1
            self.__user_streak = 0
            if self.__computer_streak > 2:
                print("I beat you {} times already".format(self.__computer_streak))


def main():
    filename = 'config.json'
    depth = 5 
    try:
        f = open(filename)
        depth = json.loads(f.read())['chain_depth']
        f.close()
    except FileNotFoundError:
        print("No file named {} can be found".format(filename))

    counter = depth
    print("Hello! Welcome to the Rock Paper Scissors game.")
    print("If you would like, you could tell me who you are so I can learn how to beat you!")
    print("If you want to have a personalized match, please type in your name. Otherwise, please press enter.\n")
    name = input("Name: ")
    rpsmachine = RPS(name)
    if name != '':
        print("Hi there {}, Let's start!".format(name))
        print("It takes me about {} rounds to learn your pattern, but once I'm there. I'm unstoppable! :).".format(counter))
    else:
        print("Well I'll assume you're just like everybody else")
        print("It takes me about {} rounds to learn your pattern and to apply that to how everyone else plays the game, but once I'm there. I'm unstoppable! :).".format(counter, ))
    input("Press enter when you are ready.")
    time.sleep(0.5)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    def isValid(user_move):
        if user_move.lower() in ('rock', 'paper', 'scissors'): 
            return True
        return False

    while True:
        print("Rock")
        time.sleep(0.4)
        print("Paper")
        time.sleep(0.4)
        print("Scissors")
        time.sleep(0.4)
        computer_move = rpsmachine.getnextmove()
        print('\nI chose', computer_move.name, '\n\n')
        print("What did you choose? (Please type 'rock', 'paper', or 'scissors.)")
        user_move = input()
        print('\n')
        while not isValid(user_move):
            print("I didn't get that. Could you please type that again?")
            user_move = input()
        rpsmachine.makemove(user_move.lower())
        rpsmachine.evalWinner(user_move = user_move, computer_move = computer_move)
        print('\n')
        counter -= 1
        if counter == 0:
            print("I think I know how to beat you now >:) Let's start really keeping track of everything.")
            rpsmachine.resetstats()
        elif counter == depth //2:
            print("Good news, I'm almost done learning how you play. I only have {} more rounds.\n".format(counter))

        if input("Press enter to play again. If you don't want to play again, press any other key + enter to quit.") != "":
            rpsmachine.quit()
            break
        print("Okay, Let's go again!")
        time.sleep(1)
    
    print("Goodbye! Thanks for playing!")



if __name__ == "__main__":
    main()
   
