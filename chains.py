import json
from rpsenum import movesenum

class Chains:
    def __init__(self, name=""):
        self.__pastmoves = list()
        self.__chain_depth = 5
        self.__chain = dict()
        self.__filename = name.lower()+'.json' 

        if name != "" and name != "allpeople":
            try:
                f = open(self.__filename)
                predictions = json.loads(f.read())
                f.close()
            except FileNotFoundError:
                predictions = self.createlayer()
        self.__chain = predictions
        print(type(self.__chain))
        print(self.__chain)

    def savefile(self):
        print(self.__filename)
        f = open(self.__filename, 'w')
        f.write(json.dumps(self.__chain))
        f.close()

    def makemove(self, move):
            if isinstance(move, str):
                move = movesenum[move.lower()]
            self.__pastmoves.append(move)
            if len(self.__pastmoves) > self.__chain_depth:
                self.__pastmoves.pop(0)

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


somechain = Chains("Nathaniel")
somechain.savefile()