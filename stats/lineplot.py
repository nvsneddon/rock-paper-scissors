import matplotlib.pyplot as plt
import json
import sys

if len(sys.argv) < 2:
    print("Please specify a file")
    exit()

try:
    f = open(sys.argv[1])
    stats = json.loads(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")
    exit()

y = stats["avg_winning_rate"]
x = stats["avg_winning_labels"]
plt.plot(x, y, color='green')
plt.xlabel("Number of times played")
plt.ylabel("Winning average of the human")
plt.title("My title")
plt.show()