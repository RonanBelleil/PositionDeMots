pip install flair

import pandas as pd

mess = pd.read_csv('messages_equilibre.csv', header = None, names = ['message', 'abusif bool'])

from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings
from flair.data import Sentence


glove_embedding = WordEmbeddings('glove')

flair_embedding_forward = FlairEmbeddings('fr-forward')
flair_embedding_backward = FlairEmbeddings('fr-backward')

stacked_embeddings = StackedEmbeddings([
                                        glove_embedding,
                                        flair_embedding_forward,
                                        flair_embedding_backward,
                                       ])
embeds = []

for i in range(len(mess)):
    stc = Sentence(str(mess.iloc[i][0]))
    stacked_embeddings.embed(stc)
    embeds.append(stc)

print(mess)

"""
for sentence in embeds:
    for token in sentence:
        print(token)
        print(token.embedding)
"""
print("embeds[0] token : ", embeds[0])
print("embeds[0][0] token embedding: ", embeds[0][0].embedding)

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
print(X[0])

tab = cross_val_score(classif, X, Y, cv=10, scoring="f1")
print(tab)

f1 = 0
for i in range(len(tab)):
  f1 = f1 + tab[i]
print(f1/len(tab))
