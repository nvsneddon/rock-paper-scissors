import json
import sys

def addfield(chain):
    if not chain:
        return
    
    chain['total'] = chain['rock']['freq']+chain['paper']['freq']+chain['scissors']['freq']

    for i, j in chain.items():
        if isinstance(j, dict):
            print(i, getdict(j))
            j['next'] = addfield(j['next'])

    return chain
    

def getdict(chain):
    if not isinstance(chain, dict):
        return chain
    for i, j in chain.items():
        if i != 'next':
            return str(i) + '\t' + str(j)

def main():
    try:
        filename = 'userdata/'+sys.argv[1] + '.json' 
        f = open(filename)
        chain = json.loads(f.read())
        chain = addfield(chain)
        f.close()
        f2 = open(filename, 'w')
        f2.write(json.dumps(chain))
        f2.close()
    except FileNotFoundError:
        print("File not found. Exiting!")
        exit(1)


if __name__ == '__main__':
    main()