import json
import random
from enum import Enum
from chain import Chain
from rpsenum import movesenum

class RPS:

    def __init__(self, name='allpeople'):
        self.__chainlist = list()
        if name != 'allpeople' or name != "":
            self.__chainlist.append(Chain(name))
        self.__chainlist.append(Chain())

    def getnextmove(self):
        predictedmoves = self.__chainlist[0].getpredictedmove()

        print(predictedmoves)

        if len(predictedmoves) > 3:
            print("something went terribly wrong")
            exit(1)
        elif len(predictedmoves) == 3:
            #We have a random choice here!
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


def main():
    rpsmachine = RPS()
    rpsmachine.makemove("rock")
    rpsmachine.makemove(2)

if __name__ == "__main__":
    main()

