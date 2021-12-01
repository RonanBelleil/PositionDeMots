import torch
from torch.utils.data import Dataset, DataLoader
import transformers
import os
import pandas as pd
import numpy as np
import numpy.linalg

from sklearn.model_selection import cross_val_score
import sklearn.model_selection
from sklearn import svm
import sklearn.metrics
from sklearn.model_selection import train_test_split

tokenizer = transformers.CamembertTokenizer.from_pretrained("camembert/camembert-large")
print("Tokenizer loaded")
model = transformers.CamembertModel.from_pretrained("camembert/camembert-large")
print("Model loaded")

def generateEmbdAndTest(filename):
    df = pd.read_csv(filename+".csv", names = ['message','label'], header=1)
    df.fillna('',inplace=True)

    textmsg = df['message'].to_list()

    print("Dataset loaded")

    X = []
    progress = 0
    progress10 = len(textmsg)//10
    for msg in textmsg:
        tokens = tokenizer.encode(msg, add_special_tokens=True)
        if len(tokens) > 512:
            tokens = tokens[:512]
        input_ids = torch.tensor(tokens).unsqueeze(0)

        last_layer = model(input_ids)[0]
        msg_emb = np.mean(last_layer[0,:,:].detach().numpy(), axis=0)
        X.append(msg_emb)
        
        progressPerCent = progress/len(textmsg)
        if progress%progress10 == 0:
            print(progressPerCent*100.)
        progress += 1

    np.save(filename+".npy", X)

    y = df['label'].to_list()
    
    cv = sklearn.model_selection.ShuffleSplit(n_splits=10, test_size=0.3, random_state=0)
    clf = svm.SVC(kernel='rbf', C=1, random_state=42)
    results = cross_val_score(clf, X, y, cv=cv, scoring="f1")
    print("---------------", filename, "---------------")
    print("F-score de la validation croisée : ", results)
    print("Moyenne des F-score", np.mean(results))
    print("--------------------------------------------")

generateEmbdAndTest("messages_equilibre_ok")
generateEmbdAndTest("alea1")
generateEmbdAndTest("alea2")
generateEmbdAndTest("alea3")
generateEmbdAndTest("alea4")
generateEmbdAndTest("alea5")
generateEmbdAndTest("POS1")
generateEmbdAndTest("POS2")
generateEmbdAndTest("POS3")
generateEmbdAndTest("POS4")
generateEmbdAndTest("POS5")
generateEmbdAndTest("LRInv1")
generateEmbdAndTest("LRInv2")
generateEmbdAndTest("LRInv3")
generateEmbdAndTest("LRInvTotal")