import random
import csv
import pandas as pd

def randomizer(sent):
    sp = str(sent).split()
    random.shuffle(sp)
    return(' '.join(sp))

mess = pd.read_csv('../Data/messages_equilibre_article.csv', header = None, names = ['message', 'abusif bool'], encoding = "utf-8")
for i in range(len(mess)):
    row = [randomizer(mess.iloc[i][0]), str(mess.iloc[i][1])]
    with open("alea4.csv", 'at', encoding="utf-8") as csvfile:
        csvw = csv.writer(csvfile, delimiter = ",", quotechar = "\"", quoting=csv.QUOTE_MINIMAL)
        csvw.writerow(row)
