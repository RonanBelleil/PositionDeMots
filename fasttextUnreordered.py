# config :
# - dataset : messages_equilibre.csv
# - modèle de représentation des mots : fasttext, cc.fr.300.bin
# - modèle de séparation des mots : spacy, fr_core_news_lg
# - modèle de classification : scikitlearn, SVM
# - évaluation : fscore sur validation croisé 10

import pandas as pd
import fasttext
import fasttext.util
import sklearn as sk
from sklearn.model_selection import cross_val_score
import sklearn.model_selection
from sklearn import svm
import sklearn.metrics
import numpy as np
import random
import spacy

def shuffle(sentense):
	parsed = nlp(sentense)
	tokens = [token.text for token in parsed]
	random.shuffle(tokens)
	return " ".join(tokens)

dt = pd.read_table("messages_equilibre.csv", header=None, sep=',', encoding="utf-8")
ft = fasttext.load_model('cc.fr.300.bin')
nlp = spacy.load("fr_core_news_lg")
X = pd.DataFrame([ft.get_sentence_vector(str(msg).replace('\n', ' ')) for msg in dt.iloc[:,0].tolist()])
y = dt.iloc[:,1]
clf = svm.SVC(kernel='linear', C=1, random_state=42)
results = cross_val_score(clf, X, y, cv=10, scoring="f1")
results
np.mean(results)
