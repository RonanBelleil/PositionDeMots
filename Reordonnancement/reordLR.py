# Permet d'inverser les branches gauche/droite de l'arbre syntaxique
# Utilisation : python reordLR.py <input> <output> [options]
# Options : depth : Profondeur à laquel on arête d'inverser les branches (-1 pour ilimité)
#           verbose : Affiche des informations sur l'avancement du script
#           help : Affiche l'aide
import time
start_time = time.time()

import pandas as pd
import spacy
import csv
import argparse

def parseTree(chunk):
	string = ""
	for subchunk in chunk.lefts:
		string += parseTree(subchunk)
	string += chunk.text + " "
	for subchunk in chunk.rights:
		string += parseTree(subchunk)
	return string

def parseTreeInv(chunk, inverseChild = 0):
	string = ""
	for subchunk in chunk.rights:
		if inverseChild != 0:
			string += parseTreeInv(subchunk, inverseChild-1)
		else:
			string += parseTree(subchunk)
	string += chunk.text + " "
	for subchunk in chunk.lefts:
		if inverseChild != 0:
			string += parseTreeInv(subchunk, inverseChild-1)
		else:
			string += parseTree(subchunk)
	return string

parser = argparse.ArgumentParser(description='Réordonnancement par inversion partiel ou total des arbres syntaxiques des massages')
parser.add_argument("input", help="Fichier du dataset")
parser.add_argument("output", help="Fichier du dataset réordonnancé")
parser.add_argument("--depth", type=int, default=1, help="Profondeur d'inversion des arbres ou -1 pour inversé tout les arbres")
parser.add_argument("--verbose", type=int, default=1, help="Affiche le detail d'execution du script")
args = parser.parse_args()

if args.verbose:
	print("[{}] Chargement du modèle de langage...".format(time.time() - start_time))
nlp = spacy.load("fr_core_news_lg")

if args.verbose:
	print("[{}] Chargement des phrases dans le modèle...".format(time.time() - start_time))
dt = pd.read_table(args.input, header=None, sep=',', encoding="utf-8")
parsed = [nlp(str(sentense)) for sentense in dt[0].tolist()]

if args.verbose:
	print("[{}] Inversion des arbres...".format(time.time() - start_time))
transformed = []
for sentense in parsed:
	outputsentense = ""
	rootChunks = [root for root in sentense if root.dep_ == 'ROOT']
	if args.depth != 0:
		for rootChunk in rootChunks:
			outputsentense += parseTreeInv(rootChunk, args.depth)
	else:
		for rootChunk in rootChunks:
			outputsentense += parseTree(rootChunk)
	transformed += [outputsentense]

if args.verbose:
	print("[{}] Écriture du fichier...".format(time.time() - start_time))
with open(args.output, 'wt', encoding="utf-8") as csvfile:
	csvw = csv.writer(csvfile, delimiter = ",", quotechar = "\"", quoting=csv.QUOTE_MINIMAL)
	for i in range(len(transformed)):
		row = [transformed[i], dt.iloc[i,1]]
		csvw.writerow(row)
if args.verbose:
	print("[{}] Fin".format(time.time() - start_time))

