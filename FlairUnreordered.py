pip install flair

import pandas as pd

mess = pd.read_csv('messages_equilibre.csv', header = None, names = ['message', 'abusif bool'])

from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings
from flair.data import Sentence


flair_embedding_forward = FlairEmbeddings('fr-forward')
flair_embedding_backward = FlairEmbeddings('fr-backward')

stacked_embeddings = StackedEmbeddings([
                                        flair_embedding_forward,
                                        flair_embedding_backward,
                                       ])
embeds = []

for i in range(len(mess)):
    stc = Sentence(str(mess.iloc[i][0]))
    stacked_embeddings.embed(stc)
    embeds.append(stc)

print(mess)

from sklearn import svm
from sklearn.model_selection import cross_val_score
import numpy as np

X = []
for i in range(len(embeds)):
  vec = embeds[i][0].embedding
  for j in range(1,len(embeds[i])):
    vec = vec + embeds[i][j].embedding
  X.append(vec.cpu().numpy()/len(embeds[i]))

Y = mess.iloc[:,1]
classif = svm.SVC(kernel='linear')
print("Dimension des vecteurs = ", len(X[0]))

tab = cross_val_score(classif, X, Y, cv=10, scoring="f1")

f1 = 0
for i in range(len(tab)):
  print("f1[", i, "] = ", tab[i])
  f1 = f1 + tab[i]
print("moyenne des f1 scores = ", f1/len(tab))
