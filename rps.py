import json
import random

from chains import Chains

class RPS:


    def __init__(self, name=''):
        self.__pastmoves = list()
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
            f2.close()
            self.__chains.append(predictions)
        except FileNotFoundError:
            print("Something went wrong!")

    def createlayer(self):
        predictions = dict()
        moves = ("rock", "paper", "scissors")
        for i in moves:
            if i not in predictions:
                newdict = dict()
                newdict["freq"] = 0
                newdict["next"] = dict()
                predictions[i] = newdict
        return predictions

    def makemove(self, move):
        self.__pastmoves.append(move)
        if len(self.__pastmoves) > self.CHAIN_DEPTH:
            self.__pastmoves.pop(0)

    def update_chains(self):
        pass

    def getpredictedmoves(self, currpredictions):
        predictednextmoves = list()
        curmax = currpredictions["rock"]["freq"]
    #Fix bug that will append object before checking other max items
        if currpredictions["scissors"]["freq"] >= curmax:
            curmax = currpredictions["scissors"]["freq"]
            predictednextmoves.append("scissors")

        if currpredictions["paper"]["freq"] >= curmax:
            curmax = currpredictions["paper"]["freq"]
            predictednextmoves.append("paper")
        
        if currpredictions["rock"]["freq"] >= curmax:
            curmax = currpredictions["rock"]["freq"]
            predictednextmoves.append("rock")

        return predictednextmoves
        
    def getnextmove(self, predictedmoves):
        if len(predictedmoves) > 3:
            print("something went wrong")
            exit(1)
        elif len(predictedmoves) == 3:
            #We have a random choice here!
            randnum = random.randint(0,2)
            if randnum == 0:
                return "rock"
            if randnum == 1:
                return "scissors"
            if randnum == 2:
                return "paper"
        elif len(predictedmoves) == 2:
            if "scissors" in predictedmoves and "paper" in predictedmoves:
                return "scissors"
            elif "rock" in predictedmoves and "scissors" in predictedmoves:
                return "rock"
            elif "rock" in predictedmoves and "paper" in predictedmoves:
                return "paper"
        elif len(predictedmoves) == 1:
            if "scissors" in predictedmoves:
                return "rock"
            if "paper" in predictedmoves:
                return "scissors"
            if "rock" in predictedmoves:
                return "paper"
        elif len(predictedmoves) < 1:
            print("Something went wrong here.")
            

rpsmachine = RPS("Nathaniel")

