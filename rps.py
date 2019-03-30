import json
import random
from enum import Enum
from chains import Chains
from rpsenum import movesenum

class RPS:

    def __init__(self, name=''):
        self.__chains = list()
        self.CHAIN_DEPTH = 5
        self.__initpredictions(name)
        

    def __initpredictions(self, name):
        if name != "" and name.lower() != "allpeople":
            try:
                f = open(name.lower() + '.json')
                predictions = json.loads(f.read())
                f.close()
                self.__chains.append(predictions)
            except FileNotFoundError:
                self.__chains.append(self.createlayer())
        try:
            f2 = open('allpeople.json')
            predictions = json.loads(f2.read())
            print(predictions)
            f2.close()
            self.__chains.append(predictions)
        except FileNotFoundError:
            print("Something went wrong!")

    def getcurrentpredictions(self):
        pass

    def createlayer(self):
        predictions = dict()
        moves = (movesenum.rock, movesenum.paper, movesenum.scissors)
        for i in moves:
            if i not in predictions:
                newdict = dict()
                newdict["freq"] = 0
                newdict["next"] = dict()
                predictions[i] = newdict
        return predictions
    
    
    def update_chains(self):
        pass

    def getpredictedmoves(self, currpredictions):
        predictednextmoves = list()
        curmax = currpredictions[movesenum.rock]["freq"]
    #Fix bug that will append object before checking other max items
        if currpredictions[movesenum.scissors]["freq"] >= curmax:
            curmax = currpredictions[movesenum.scissors]["freq"]
            predictednextmoves.append(movesenum.scissors)

        if currpredictions[movesenum.paper]["freq"] >= curmax:
            curmax = currpredictions[movesenum.paper]["freq"]
            predictednextmoves.append(movesenum.paper)
        
        if currpredictions[movesenum.rock]["freq"] >= curmax:
            curmax = currpredictions[movesenum.rock]["freq"]
            predictednextmoves.append(movesenum.rock)

        return predictednextmoves

    def getpastmoves(self):
        return self.__pastmoves
        
    def getnextmove(self, predictedmoves):
        if len(predictedmoves) > 3:
            print("something went wrong")
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

    def getchain(self):
        return self.__chains
            

def main():
    rpsmachine = RPS("Nathaniel")


if __name__ == "__main__":
    main()

