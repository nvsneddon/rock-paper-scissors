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
print(spstats.ttest_1samp(losses, 0.33))
print(stats.stdev(losses))