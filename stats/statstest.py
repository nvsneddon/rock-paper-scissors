import statistics as stats
import scipy.stats as spstats
import json


myfile = "all_computer_losses.json"

try:
    f = open(myfile)
    losses = json.loads(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")
    exit()
tstat, pvalue = spstats.ttest_1samp(losses, 0.33)

print("The computer has lost", sum(losses), "games")
print("The computer has played", len(losses), "games")
print("The average of the losses is {:1.4}".format(sum(losses)/len(losses)))
print("The Std dev is {:1.4}".format(stats.stdev(losses)))

print("The stats test gives a T value of {:2.6} and a pvalue of {:4.4}".format(tstat, pvalue))