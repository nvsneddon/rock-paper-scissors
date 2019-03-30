import json
import random
import time

from enum import Enum
from chain import Chain
from rpsenum import movesenum
from datetime import datetime

class RPS:

    def __init__(self, name='allpeople'):
        self.__chainlist = list()
        if name != 'allpeople' or name != "":
            self.__chainlist.append(Chain(name))
        self.__chainlist.append(Chain())

    def getnextmove(self):
        predictedmoves = self.__chainlist[0].getpredictedmove()

        if len(predictedmoves) > 3:
            print("something went terribly wrong")
            exit(1)
        elif len(predictedmoves) == 3:
            #We have a random choice here!
            random.seed(datetime.now().microsecond % 10000)
            randnum = random.randint(0,2)
            if randnum == 0:
                return movesenum.rock.name
            if randnum == 1:
                return movesenum.scissors.name
            if randnum == 2:
                return movesenum.paper.name
        elif len(predictedmoves) == 2:
            if movesenum.scissors in predictedmoves and movesenum.paper in predictedmoves:
                return movesenum.scissors.name
            elif movesenum.rock in predictedmoves and movesenum.scissors in predictedmoves:
                return movesenum.rock.name
            elif movesenum.rock in predictedmoves and movesenum.paper in predictedmoves:
                return movesenum.paper.name
        elif len(predictedmoves) == 1:
            if movesenum.scissors in predictedmoves:
                return movesenum.rock.name
            if movesenum.paper in predictedmoves:
                return movesenum.scissors.name
            if movesenum.rock in predictedmoves:
                return movesenum.paper.name
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
        for i in self.__chainlist:
            i.savefile()
        print("Goodbye! Thanks for playing!")


def main():
    print("Hello! Welcome to the Rock Paper Scissors game.")
    print("If you would like, you could tell me who you are so I can learn how to beat you!")
    print("If you want to have a personalized match, please type in your name. Otherwise, please press enter.\n")
    rpsmachine = RPS(input("Name: "))

    while True:
        print("Rock")
        time.sleep(0.4)
        print("Paper")
        time.sleep(0.4)
        print("Scissors")
        time.sleep(0.4)
        print('\nI chose', rpsmachine.getnextmove(), '\n\n')




if __name__ == "__main__":
    main()

