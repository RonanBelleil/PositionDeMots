import re
import matplotlib
import matplotlib.pyplot
import numpy

# alea
X = {"{'alea1.npy': 1.0}": 0.8412958651121036,
 "{'alea2.npy': 1.0}": 0.8322573662435993,
 "{'alea3.npy': 1.0}": 0.8484820086264865,
 "{'alea4.npy': 1.0}": 0.8378882523069919,
 "{'alea5.npy': 1.0}": 0.8347224462527565,
 "{'alea1.npy': 0.5, 'alea2.npy': 0.5}": 0.8426790994138582,
 "{'alea1.npy': 0.5, 'alea3.npy': 0.5}": 0.8457037444382746,
 "{'alea1.npy': 0.5, 'alea4.npy': 0.5}": 0.8447314478670285,
 "{'alea1.npy': 0.5, 'alea5.npy': 0.5}": 0.8400047549955346,
 "{'alea2.npy': 0.5, 'alea3.npy': 0.5}": 0.8490908277962189,
 "{'alea2.npy': 0.5, 'alea4.npy': 0.5}": 0.840119435722628,
 "{'alea2.npy': 0.5, 'alea5.npy': 0.5}": 0.8424935731279325,
 "{'alea3.npy': 0.5, 'alea4.npy': 0.5}": 0.8473080450642916,
 "{'alea3.npy': 0.5, 'alea5.npy': 0.5}": 0.850208495348965,
 "{'alea4.npy': 0.5, 'alea5.npy': 0.5}": 0.8434234417826143,
 "{'alea1.npy': 0.333, 'alea2.npy': 0.333, 'alea3.npy': 0.333}": 0.8486489398065645,
 "{'alea1.npy': 0.333, 'alea2.npy': 0.333, 'alea4.npy': 0.333}": 0.8419053947242607,
 "{'alea1.npy': 0.333, 'alea2.npy': 0.333, 'alea5.npy': 0.333}": 0.8452569479680146,
 "{'alea1.npy': 0.333, 'alea3.npy': 0.333, 'alea4.npy': 0.333}": 0.8502565355273427,
 "{'alea1.npy': 0.333, 'alea3.npy': 0.333, 'alea5.npy': 0.333}": 0.8478955258255967,
 "{'alea1.npy': 0.333, 'alea4.npy': 0.333, 'alea5.npy': 0.333}": 0.8463913296242875,
 "{'alea2.npy': 0.333, 'alea3.npy': 0.333, 'alea4.npy': 0.333}": 0.8434243809100168,
 "{'alea2.npy': 0.333, 'alea3.npy': 0.333, 'alea5.npy': 0.333}": 0.8498302192581647,
 "{'alea2.npy': 0.333, 'alea4.npy': 0.333, 'alea5.npy': 0.333}": 0.8426210702147552,
 "{'alea3.npy': 0.333, 'alea4.npy': 0.333, 'alea5.npy': 0.333}": 0.8485844596309343,
 "{'alea1.npy': 0.25, 'alea2.npy': 0.25, 'alea3.npy': 0.25, 'alea4.npy': 0.25}": 0.8482665339074984,
 "{'alea1.npy': 0.25, 'alea2.npy': 0.25, 'alea3.npy': 0.25, 'alea5.npy': 0.25}": 0.8505262434845399,
 "{'alea1.npy': 0.25, 'alea2.npy': 0.25, 'alea4.npy': 0.25, 'alea5.npy': 0.25}": 0.8431609821519706,
 "{'alea1.npy': 0.25, 'alea3.npy': 0.25, 'alea4.npy': 0.25, 'alea5.npy': 0.25}": 0.850255118334354,
 "{'alea2.npy': 0.25, 'alea3.npy': 0.25, 'alea4.npy': 0.25, 'alea5.npy': 0.25}": 0.8495908384147162,
 "{'alea1.npy': 0.2, 'alea2.npy': 0.2, 'alea3.npy': 0.2, 'alea4.npy': 0.2, 'alea5.npy': 0.2}": 0.849112379650293}

aleaN = [{k:v for k,v in X.items() if "alea"+str(i+1) in k} for i in range(5)]
aleaN = [{re.sub("'alea([1-5]).npy': [0-9.]+(,)?( )?", "\\1\\2", k)[1:-1]:v for k,v in X.items() if "alea"+str(i+1) in k} for i in range(5)]

xref = [list(aleaN[j].values())[0] for j in range(5)]

for i in range(5):
	matplotlib.pyplot.clf()
	matplotlib.pyplot.bar(list(aleaN[i].keys())[1:], list(aleaN[i].values())[1:], width=0.6)
	matplotlib.pyplot.ylim(0.8, 0.9)
	matplotlib.pyplot.xticks(rotation=30, ha='right')
	matplotlib.pyplot.axhline(min(xref), color='red')
	matplotlib.pyplot.axhline(max(xref), color='red')
	matplotlib.pyplot.axhline(list(aleaN[i].values())[0], color='k')
	matplotlib.pyplot.savefig("fig_mix_alea_ref"+str(i+1)+".svg")

# POS
X = {"{'POS1.npy': 1.0}": 0.8511136963179033,
 "{'POS2.npy': 1.0}": 0.8510651927924092,
 "{'POS3.npy': 1.0}": 0.8563627159776992,
 "{'POS4.npy': 1.0}": 0.855185594141408,
 "{'POS5.npy': 1.0}": 0.8626254624583733,
 "{'POS1.npy': 0.5, 'POS2.npy': 0.5}": 0.8543822683232406,
 "{'POS1.npy': 0.5, 'POS3.npy': 0.5}": 0.8564762629421241,
 "{'POS1.npy': 0.5, 'POS4.npy': 0.5}": 0.8533085232789469,
 "{'POS1.npy': 0.5, 'POS5.npy': 0.5}": 0.8595978528304,
 "{'POS2.npy': 0.5, 'POS3.npy': 0.5}": 0.8552115307044066,
 "{'POS2.npy': 0.5, 'POS4.npy': 0.5}": 0.8551609771347287,
 "{'POS2.npy': 0.5, 'POS5.npy': 0.5}": 0.8573197524933607,
 "{'POS3.npy': 0.5, 'POS4.npy': 0.5}": 0.8563794203451873,
 "{'POS3.npy': 0.5, 'POS5.npy': 0.5}": 0.8654436500800315,
 "{'POS4.npy': 0.5, 'POS5.npy': 0.5}": 0.859335597111583,
 "{'POS1.npy': 0.333, 'POS2.npy': 0.333, 'POS3.npy': 0.333}": 0.8568034557946312,
 "{'POS1.npy': 0.333, 'POS2.npy': 0.333, 'POS4.npy': 0.333}": 0.855664152683415,
 "{'POS1.npy': 0.333, 'POS2.npy': 0.333, 'POS5.npy': 0.333}": 0.8582975402801368,
 "{'POS1.npy': 0.333, 'POS3.npy': 0.333, 'POS4.npy': 0.333}": 0.8558473331735689,
 "{'POS1.npy': 0.333, 'POS3.npy': 0.333, 'POS5.npy': 0.333}": 0.8641505885626695,
 "{'POS1.npy': 0.333, 'POS4.npy': 0.333, 'POS5.npy': 0.333}": 0.8593515547349192,
 "{'POS2.npy': 0.333, 'POS3.npy': 0.333, 'POS4.npy': 0.333}": 0.858002092088227,
 "{'POS2.npy': 0.333, 'POS3.npy': 0.333, 'POS5.npy': 0.333}": 0.8614697545791195,
 "{'POS2.npy': 0.333, 'POS4.npy': 0.333, 'POS5.npy': 0.333}": 0.8596067736840334,
 "{'POS3.npy': 0.333, 'POS4.npy': 0.333, 'POS5.npy': 0.333}": 0.8602427766368164,
 "{'POS1.npy': 0.25, 'POS2.npy': 0.25, 'POS3.npy': 0.25, 'POS4.npy': 0.25}": 0.8545596154612951,
 "{'POS1.npy': 0.25, 'POS2.npy': 0.25, 'POS3.npy': 0.25, 'POS5.npy': 0.25}": 0.8615078391824967,
 "{'POS1.npy': 0.25, 'POS2.npy': 0.25, 'POS4.npy': 0.25, 'POS5.npy': 0.25}": 0.8586196784595275,
 "{'POS1.npy': 0.25, 'POS3.npy': 0.25, 'POS4.npy': 0.25, 'POS5.npy': 0.25}": 0.8594498522168982,
 "{'POS2.npy': 0.25, 'POS3.npy': 0.25, 'POS4.npy': 0.25, 'POS5.npy': 0.25}": 0.8601537311561293,
 "{'POS1.npy': 0.2, 'POS2.npy': 0.2, 'POS3.npy': 0.2, 'POS4.npy': 0.2, 'POS5.npy': 0.2}": 0.8590571589983425}

POSN = [{k:v for k,v in X.items() if "POS"+str(i+1) in k} for i in range(5)]
POSN = [{re.sub("'POS([1-5]).npy': [0-9.]+(,)?( )?", "\\1\\2", k)[1:-1]:v for k,v in X.items() if "POS"+str(i+1) in k} for i in range(5)]

xref = [list(POSN[j].values())[0] for j in range(5)]

for i in range(5):
	matplotlib.pyplot.clf()
	matplotlib.pyplot.bar(list(POSN[i].keys())[1:], list(POSN[i].values())[1:], width=0.6)
	matplotlib.pyplot.ylim(0.8, 0.9)
	matplotlib.pyplot.xticks(rotation=30, ha='right')
	matplotlib.pyplot.axhline(min(xref), color='red')
	matplotlib.pyplot.axhline(max(xref), color='red')
	matplotlib.pyplot.axhline(list(POSN[i].values())[0], color='k')
	matplotlib.pyplot.savefig("fig_mix_POS_ref"+str(i+1)+".svg")


# LRInv
X = {"{'LRInv1.npy': 1.0}": 0.8618716441425647,
 "{'LRInv2.npy': 1.0}": 0.845405935963117,
 "{'LRInv3.npy': 1.0}": 0.8461662207890495,
 "{'LRInvT.npy': 1.0}": 0.8423471257324868,
 "{'LRInv1.npy': 0.5, 'LRInv2.npy': 0.5}": 0.8556988463535168,
 "{'LRInv1.npy': 0.5, 'LRInv3.npy': 0.5}": 0.8575043019423182,
 "{'LRInv1.npy': 0.5, 'LRInvT.npy': 0.5}": 0.8565201273375378,
 "{'LRInv2.npy': 0.5, 'LRInv3.npy': 0.5}": 0.84572764279366,
 "{'LRInv2.npy': 0.5, 'LRInvT.npy': 0.5}": 0.846135683409921,
 "{'LRInv3.npy': 0.5, 'LRInvT.npy': 0.5}": 0.8436447342148569,
 "{'LRInv1.npy': 0.333, 'LRInv2.npy': 0.333, 'LRInv3.npy': 0.333}": 0.8505427677125335,
 "{'LRInv1.npy': 0.333, 'LRInv2.npy': 0.333, 'LRInvT.npy': 0.333}": 0.8500340216335894,
 "{'LRInv1.npy': 0.333, 'LRInv3.npy': 0.333, 'LRInvT.npy': 0.333}": 0.8499422453303586,
 "{'LRInv2.npy': 0.333, 'LRInv3.npy': 0.333, 'LRInvT.npy': 0.333}": 0.8466787194280808,
 "{'LRInv1.npy': 0.25, 'LRInv2.npy': 0.25, 'LRInv3.npy': 0.25, 'LRInvT.npy': 0.25}": 0.8486474036242775}

L = ["1","2","3","T"]

LRInvN = [{k:v for k,v in X.items() if "LRInv"+L[i] in k} for i in range(4)]
LRInvN = [{re.sub("'LRInv([1-5T]).npy': [0-9.]+(,)?( )?", "\\1\\2", k)[1:-1]:v for k,v in X.items() if "LRInv"+L[i] in k} for i in range(4)]

xref = [list(LRInvN[j].values())[0] for j in range(4)]

for i in range(4):
	matplotlib.pyplot.clf()
	matplotlib.pyplot.bar(list(LRInvN[i].keys())[1:], list(LRInvN[i].values())[1:], width=0.6)
	matplotlib.pyplot.ylim(0.8, 0.9)
	matplotlib.pyplot.xticks(rotation=30, ha='right')
	matplotlib.pyplot.axhline(min(xref), color='red')
	matplotlib.pyplot.axhline(max(xref), color='red')
	matplotlib.pyplot.axhline(list(LRInvN[i].values())[0], color='k')
	matplotlib.pyplot.savefig("fig_mix_LRInv_ref"+L[i]+".svg")

# Ref + Autre, concat
X = {"{'messages_equilibre_ok.npy': 1.0, 'alea1.npy': 1.0}": 0.8665668197558084,
 "{'messages_equilibre_ok.npy': 1.0, 'alea2.npy': 1.0}": 0.8665204138939211,
 "{'messages_equilibre_ok.npy': 1.0, 'alea3.npy': 1.0}": 0.865357368040099,
 "{'messages_equilibre_ok.npy': 1.0, 'alea4.npy': 1.0}": 0.8600617222773858,
 "{'messages_equilibre_ok.npy': 1.0, 'alea5.npy': 1.0}": 0.863035359421682,
 "{'messages_equilibre_ok.npy': 1.0, 'POS1.npy': 1.0}": 0.8646244439561857,
 "{'messages_equilibre_ok.npy': 1.0, 'POS2.npy': 1.0}": 0.8661818816636163,
 "{'messages_equilibre_ok.npy': 1.0, 'POS3.npy': 1.0}": 0.8677173510405456,
 "{'messages_equilibre_ok.npy': 1.0, 'POS4.npy': 1.0}": 0.865559184932154,
 "{'messages_equilibre_ok.npy': 1.0, 'POS5.npy': 1.0}": 0.8700548052777922,
 "{'messages_equilibre_ok.npy': 1.0, 'LRInv1.npy': 1.0}": 0.8754953347278122,
 "{'messages_equilibre_ok.npy': 1.0, 'LRInv2.npy': 1.0}": 0.8705370535276717,
 "{'messages_equilibre_ok.npy': 1.0, 'LRInv3.npy': 1.0}": 0.8705844282429988,
 "{'messages_equilibre_ok.npy': 1.0, 'LRInvTotal.npy': 1.0}": 0.8724696307894115}

Xrefs = {"alea1": 0.8412958651121036,
 "alea2": 0.8322573662435993,
 "alea3": 0.8484820086264865,
 "alea4": 0.8378882523069919,
 "alea5": 0.8347224462527565,
 "POS1": 0.8511136963179033,
 "POS2": 0.8510651927924092,
 "POS3": 0.8563627159776992,
 "POS4": 0.855185594141408,
 "POS5": 0.8626254624583733,
 "LRInv1": 0.8618716441425647,
 "LRInv2": 0.845405935963117,
 "LRInv3": 0.8461662207890495,
 "LRInvTotal": 0.8423471257324868}

xref = 0.8692509234307005

P = numpy.arange(len(X))

ax = matplotlib.pyplot.subplot(111)
ax.bar(P, list(X.values()), width=0.4, label = "Concaténation avec et sans réordonnancement")
ax.bar(P+0.4, list(Xrefs.values()), width=0.4, label = "Référence")
ax.set_ylim(0.8, 0.9)
matplotlib.pyplot.xticks(P, list(Xrefs.keys()), rotation=30, ha='center')
matplotlib.pyplot.ylabel("Score")
matplotlib.pyplot.axhline(xref, color='k')
matplotlib.pyplot.legend()
matplotlib.pyplot.savefig("fig_conc_vs_ref.svg")

# Reference + ajout progressif par ordre décroissant des résultats, concat
X = {"REF": 0.8692509234307005,
 "+POS5": 0.8700548052777922,
 "+LRInv1": 0.8724492723039502,
 "+POS3": 0.8722116959823845,
 "+POS4": 0.8711704120255087,
 "+POS1": 0.8687653120035286,
 "+POS2": 0.8675988169513605,
 "+alea3": 0.8656985625767726,
 "+LRInv3": 0.8647434170326452,
 "+LRInv2": 0.8642617651820746,
 "+LRInvTotal": 0.8624805090051428,
 "+alea1": 0.8620121468878121,
 "+alea4": 0.8610701027580886,
 "+alea5": 0.8610168326567631,
 "+alea2": 0.8599283020451981}

xref = 0.8692509234307005

matplotlib.pyplot.clf()
matplotlib.pyplot.bar(X.keys(), X.values(), width=.8)
matplotlib.pyplot.ylim(0.8, 0.9)
matplotlib.pyplot.xticks(rotation=30, ha='right')
matplotlib.pyplot.axhline(xref, color='k')
matplotlib.pyplot.savefig("fig_conc_decr.svg")


# Reference + ajout progressif par ordre croissant des résultats, concat
X = {"REF": 0.8692509234307005,
 "+alea2": 0.8665204138939211,
 "+alea5": 0.86130852463299,
 "+alea4": 0.8568005480461945,
 "+alea1": 0.8534425418006005,
 "+LRInvTotal": 0.8575473023168143,
 "+LRInv2": 0.8596847504613818,
 "+LRInv3": 0.8601757638246583,
 "+alea3": 0.8588178486059126,
 "+POS2": 0.859115813844244,
 "+POS1": 0.8574725077460833,
 "+POS4": 0.8585295291679769,
 "+POS3": 0.8586633535489103,
 "+LRInv1": 0.8590139868539521,
 "+POS5": 0.8599283020451981}

xref = 0.8692509234307005

matplotlib.pyplot.clf()
matplotlib.pyplot.bar(X.keys(), X.values(), width=.8)
matplotlib.pyplot.ylim(0.8, 0.9)
matplotlib.pyplot.xticks(rotation=30, ha='right')
matplotlib.pyplot.axhline(xref, color='k')
matplotlib.pyplot.savefig("fig_conc_crois.svg")

# Ajout progressif par ordre décroissant des résultats + Reference, concat
X = {"POS5": 0.8626254624583733,
 "+LRInv1": 0.866432697950305,
 "+POS3": 0.8693883848763699,
 "+POS4": 0.8653997076722707,
 "+POS1": 0.8638226894488232,
 "+POS2": 0.8624304329668716,
 "+alea3": 0.8599480873689493,
 "+LRInv3": 0.8614698327216581,
 "+LRInv2": 0.8615434321183001,
 "+LRInvTotal": 0.8608581349239628,
 "+alea1": 0.8591254592599021,
 "+alea4": 0.8582489911539829,
 "+alea5": 0.857362143651852,
 "+alea2": 0.8578517387458664,
 "+REF": 0.8599283020451981}

xref = 0.8692509234307005

matplotlib.pyplot.clf()
matplotlib.pyplot.bar(X.keys(), X.values(), width=.8)
matplotlib.pyplot.ylim(0.8, 0.9)
matplotlib.pyplot.xticks(rotation=30, ha='right')
matplotlib.pyplot.axhline(xref, color='k')
matplotlib.pyplot.savefig("fig_conc_decr2.svg")

# Ajout progressif par ordre croissant des résultats + Reference, concat
X = {"alea2": 0.8322573662435993,
 "+alea5": 0.8415910624982994,
 "+alea4": 0.8390159091657479,
 "+alea1": 0.8443708421051388,
 "+LRInvTotal": 0.8479211192160794,
 "+LRInv2": 0.8501529359714375,
 "+LRInv3": 0.8533765259009349,
 "+alea3": 0.8509386783741537,
 "+POS2": 0.8521751875742597,
 "+POS1": 0.8535278560598002,
 "+POS4": 0.8544960806233535,
 "+POS3": 0.854768781833841,
 "+LRInv1": 0.8556144286556566,
 "+POS5": 0.8578517387458664,
 "+REF": 0.8599283020451981}

xref = 0.8692509234307005

matplotlib.pyplot.clf()
matplotlib.pyplot.bar(X.keys(), X.values(), width=.8)
matplotlib.pyplot.ylim(0.8, 0.9)
matplotlib.pyplot.xticks(rotation=30, ha='right')
matplotlib.pyplot.axhline(xref, color='k')
matplotlib.pyplot.savefig("fig_conc_crois2.svg")


# All
X = {"R": 0.8692509234307005,
 "A": 0.8412958651121036,
 "P": 0.8511136963179033,
 "S1": 0.8618716441425647,
 "S2": 0.845405935963117,
 "T": 0.8423471257324868,
 "RA": 0.8622280100582425,
 "RP": 0.8673113036372152,
 "RS1": 0.8752999646067596,
 "RS2": 0.8722720528174056,
 "RT": 0.8696675341042228,
 "AP": 0.854306163366417,
 "AS1": 0.8591390588781813,
 "AS2": 0.850258035706592,
 "AT": 0.8512875441890155,
 "PS1": 0.8608590980750934,
 "PS2": 0.8565673584962312,
 "PT": 0.8531742590350312,
 "S1S2": 0.8556988463535168,
 "S1T": 0.8565201273375378,
 "S2T": 0.846135683409921,
 "RAP": 0.8646007581313304,
 "RAS1": 0.8693478385286454,
 "RAS2": 0.8650919330304901,
 "RAT": 0.8655461666116082,
 "RPS1": 0.868547635370746,
 "RPS2": 0.8643550145001344,
 "RPT": 0.8632753759534179,
 "RS1S2": 0.8717550033329559,
 "RS1T": 0.8724138907585326,
 "RS2T": 0.8639524294753572,
 "APS1": 0.8618291165913723,
 "APS2": 0.8553621067835451,
 "APT": 0.8566506001514295,
 "AS1S2": 0.8557364459829543,
 "AS1T": 0.8551264409717356,
 "AS2T": 0.8526089003973066,
 "PS1S2": 0.8601372686277081,
 "PS1T": 0.8574737724608997,
 "PS2T": 0.8527818354998047,
 "S1S2T": 0.8500340216335894,
 "RAPS1": 0.8646470582702193,
 "RAPS2": 0.8628250593921626,
 "RAPT": 0.8626785238548882,
 "RAS1S2": 0.8667300635827777,
 "RAS1T": 0.8668537026885268,
 "RAS2T": 0.8628769031711133,
 "RPS1S2": 0.865626875942675,
 "RPS1T": 0.8651673854083184,
 "RPS2T": 0.861496060318251,
 "RS1S2T": 0.8658261001740035,
 "APS1S2": 0.8607419010655993,
 "APS1T": 0.8615344210972651,
 "APS2T": 0.856190520213568,
 "AS1S2T": 0.8544331881195101,
 "PS1S2T": 0.8551472118781197,
 "RAPS1S2": 0.8669287007983705,
 "RAPS1T": 0.8662816133748971,
 "RAPS2T": 0.8618656949523714,
 "RAS1S2T": 0.8662050333918536,
 "RPS1S2T": 0.8645164559145913,
 "APS1S2T": 0.859592102833397,
 "RAPS1S2T": 0.8646705774468778}

matplotlib.pyplot.clf()
matplotlib.pyplot.barh(list(X.keys()), list(X.values()))
matplotlib.pyplot.xlim(0.8, 0.9)
matplotlib.pyplot.axvline(0.8692509234307005, color='k')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(20, 30)
matplotlib.pyplot.savefig("fig_mix_Total.svg")
