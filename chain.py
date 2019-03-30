import json
from rpsenum import movesenum

class Chain:
    def __init__(self, name="allpeople"):
        self.__pastmoves = list()
        self.__chain_depth = 5
        self.__chain = dict()
        self.__filename = name.lower()+'.json' 

        try:
            f = open(self.__filename)
            predictions = json.loads(f.read())
            f.close()
        except FileNotFoundError:
            predictions = self.__createlayer()
        self.__chain = predictions

    def __updateChain(self, chain=dict(), level=0, start=True):
        if start:
            return self.__updateChain(self.__chain, start=False)
            

        if level >= self.__chain_depth or level >= len(self.__pastmoves):
            raise ValueError("The level is out of bounds.")

        if not chain:
            chain = self.__createlayer()

        if level == self.__chain_depth - 1 or level == len(self.__pastmoves)-1:
            chain[self.__pastmoves[level].name]["freq"] += 1
            return chain

        chain[self.__pastmoves[level].name]["next"] = self.__updateChain(chain[self.__pastmoves[level].name]['next'], level=level+1, start=False)
        return chain


    def savefile(self):
        f = open(self.__filename, 'w')
        f.write(json.dumps(self.__chain))
        f.close()

    def makemove(self, move):
            if isinstance(move, str):
                move = movesenum[move.lower()]
            self.__pastmoves.append(move)
            if len(self.__pastmoves) > self.__chain_depth:
                self.__pastmoves.pop(0)
            self.__chain = self.__updateChain()

    def __createlayer(self):
        predictions = dict()
        moves = ("rock", "paper", "scissors")
        for i in moves:
            if i not in predictions:
                newdict = dict()
                newdict["freq"] = 0
                newdict["next"] = dict()
                predictions[i] = newdict
        return predictions

    def getpredictedmove(self):
        movedict = self.__chain.copy()
        for i in self.__pastmoves:
            movedict = movedict[i.name]['next']

        if not movedict:
            return [movesenum.rock, movesenum.paper, movesenum.scissors] 

        predictednextmoves = list()
        curmax = 0 

        for i in (movesenum.rock, movesenum.paper, movesenum.scissors):
            if curmax < movedict[i.name]['freq']:
                curmax = movedict[i.name]['freq']
                predictednextmoves = list()
                predictednextmoves.append(i)
            elif curmax == movedict[i.name]['freq']:
                predictednextmoves.append(i)

        return predictednextmoves


def main():
    somechain = Chain()

    print(somechain.getpredictedmove())

    #somechain.savefile()

if __name__ == "__main__":
    main()