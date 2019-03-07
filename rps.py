import json
import random

pastmoves = list()

def initpredictions(name):
    try:
        f = open(name.lower() + '.json')
        predictions = json.loads(f.read())
        f.close()
    except FileNotFoundError:
        predictions = dict()

    moves = ("rock", "paper", "scissors")
    for i in moves:
        if i not in predictions:
            newdict = dict()
            newdict["freq"] = 0
            newdict["next"] = dict()
            predictions[i] = newdict
    return predictions

def makemove(move):
    pastmoves.append(move)


def getpredictedmoves(currpredictions):
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
    
def getnextmove(predictedmoves):
    if len(predictedmoves) > 3:
        print("something went wrong")
        exit(1)
    elif len(predictedmoves) == 3:
        pass
        #make random choice because it doesn't matter
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
    elif len(predictedmoves) == 0:
        randnum = random.randint(0,2)
        if randnum == 0:
            return "rock"
        if randnum == 1:
            return "scissors"
        if randnum == 2:
            return "paper"

print(initpredictions("Nathaniel"))
