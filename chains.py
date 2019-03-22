import json

class Chains:
    def __init__(self, name=""):
        self.__chains = list()
        if name != "" and name != "allpeople":
            try:
                f = open(name.lower() + '.json')
                predictions = json.loads(f.read())
                f.close()
                self.__chains.append(predictions)
            except FileNotFoundError:
                self.__chains.append(createlayer())
        self.__chains.append()

def createlayer():
    predictions = dict()
    moves = ("rock", "paper", "scissors")
    for i in moves:
        if i not in predictions:
            newdict = dict()
            newdict["freq"] = 0
            newdict["next"] = dict()
            predictions[i] = newdict
    return predictions