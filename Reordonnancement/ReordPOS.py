import spacy
import random
import csv
import pandas as pd

nlp = spacy.load("fr_core_news_sm")

def shufflePOS(phrase):
    doc = nlp(phrase)

    dict = {}
    ordre = []
    for token in doc:
        ordre.append(token.pos_)
        if(token.pos_ in dict):
            dict[token.pos_] = dict[token.pos_] + [token.text]
        else:
            dict[token.pos_] = [token.text]

    newList = []

    for ind in range(len(doc)):
        cat = ordre[ind]
        seq = dict[cat]
        mot = seq.pop(random.randint(0,len(seq)-1))
        newList.append(mot)

    newPhrase = ' '.join(newList)
    return newPhrase

mess = pd.read_csv('../Data/messages_equilibre_article.csv', header = None, names = ['message', 'abusif bool'], encoding = "utf-8")
for i in range(len(mess)):
    row = [shufflePOS(mess.iloc[i][0]), str(mess.iloc[i][1])]
    with open("POS1.csv", 'at', encoding="utf-8") as csvfile:
        csvw = csv.writer(csvfile, delimiter = ",", quotechar = "\"", quoting=csv.QUOTE_MINIMAL)
        csvw.writerow(row)
