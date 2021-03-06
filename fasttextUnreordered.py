# config :
# - modèle de représentation des mots : fasttext, cc.fr.300.bin
# - modèle de séparation des mots : fasttext (par espace)
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
import numpy.linalg
import random
import argparse

def sentenseVector(model, sentense):
	return model.get_sentence_vector(sentense)

parser = argparse.ArgumentParser(description='Approche fasttext avec la tache de classification avec SVM')
parser.add_argument("input", help="Fichier du dataset")
args = parser.parse_args()

dt = pd.read_table(args.input, header=None, sep=',', encoding="utf-8")
ft = fasttext.load_model('cc.fr.300.bin')
#ft = WordEmbeddings('fr')
X = pd.DataFrame([sentenseVector(ft, str(msg).replace('\n', ' ')) for msg in dt.iloc[:,0].tolist()])
y = dt.iloc[:,1]
clf = svm.SVC(kernel='linear', C=1, random_state=42)
results = cross_val_score(clf, X, y, cv=10, scoring="f1")
print("F-score de la validation croisée : ", results)
print("Moyenne des F-score", np.mean(results))
