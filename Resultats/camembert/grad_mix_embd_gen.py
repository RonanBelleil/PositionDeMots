import pandas
import matplotlib

gradTable = [{"{'alea1.npy': 1.0}": 0.8412958651121036,
 "{'messages_equilibre_ok.npy': 0.1, 'alea1.npy': 0.9}": 0.8459419014017893,
 "{'messages_equilibre_ok.npy': 0.2, 'alea1.npy': 0.8}": 0.8501402871732167,
 "{'messages_equilibre_ok.npy': 0.30000000000000004, 'alea1.npy': 0.7}": 0.8556410486399276,
 "{'messages_equilibre_ok.npy': 0.4, 'alea1.npy': 0.6}": 0.8577483853283263,
 "{'messages_equilibre_ok.npy': 0.5, 'alea1.npy': 0.5}": 0.8622280100582425,
 "{'messages_equilibre_ok.npy': 0.6, 'alea1.npy': 0.4}": 0.8667360394434895,
 "{'messages_equilibre_ok.npy': 0.7000000000000001, 'alea1.npy': 0.29999999999999993}": 0.8699865943482225,
 "{'messages_equilibre_ok.npy': 0.8, 'alea1.npy': 0.19999999999999996}": 0.8699485783049526,
 "{'messages_equilibre_ok.npy': 0.9, 'alea1.npy': 0.09999999999999998}": 0.868438650771904,
 "{'messages_equilibre_ok.npy': 1.": 0.8692509234307005},
{"{'POS1.npy': 1.0}": 0.8511136963179033,
 "{'messages_equilibre_ok.npy': 0.1, 'POS1.npy': 0.9}": 0.8564809123488937,
 "{'messages_equilibre_ok.npy': 0.2, 'POS1.npy': 0.8}": 0.8594499742051269,
 "{'messages_equilibre_ok.npy': 0.30000000000000004, 'POS1.npy': 0.7}": 0.8622584760026568,
 "{'messages_equilibre_ok.npy': 0.4, 'POS1.npy': 0.6}": 0.8632591452063624,
 "{'messages_equilibre_ok.npy': 0.5, 'POS1.npy': 0.5}": 0.8673113036372152,
 "{'messages_equilibre_ok.npy': 0.6, 'POS1.npy': 0.4}": 0.8695764950225982,
 "{'messages_equilibre_ok.npy': 0.7000000000000001, 'POS1.npy': 0.29999999999999993}": 0.8699288794368731,
 "{'messages_equilibre_ok.npy': 0.8, 'POS1.npy': 0.19999999999999996}": 0.8689651197506973,
 "{'messages_equilibre_ok.npy': 0.9, 'POS1.npy': 0.09999999999999998}": 0.8684991714107388,
 "{'messages_equilibre_ok.npy': 1.": 0.8692509234307005},
{"{'LRInv1.npy': 1.0}": 0.8618716441425647,
 "{'messages_equilibre_ok.npy': 0.1, 'LRInv1.npy': 0.9}": 0.8657766368421489,
 "{'messages_equilibre_ok.npy': 0.2, 'LRInv1.npy': 0.8}": 0.8706280936753986,
 "{'messages_equilibre_ok.npy': 0.30000000000000004, 'LRInv1.npy': 0.7}": 0.8716583057949896,
 "{'messages_equilibre_ok.npy': 0.4, 'LRInv1.npy': 0.6}": 0.8737644062777988,
 "{'messages_equilibre_ok.npy': 0.5, 'LRInv1.npy': 0.5}": 0.8752999646067596,
 "{'messages_equilibre_ok.npy': 0.6, 'LRInv1.npy': 0.4}": 0.8735407032148979,
 "{'messages_equilibre_ok.npy': 0.7000000000000001, 'LRInv1.npy': 0.29999999999999993}": 0.8736940348950937,
 "{'messages_equilibre_ok.npy': 0.8, 'LRInv1.npy': 0.19999999999999996}": 0.871188226009304,
 "{'messages_equilibre_ok.npy': 0.9, 'LRInv1.npy': 0.09999999999999998}": 0.8710921769137041,
 "{'messages_equilibre_ok.npy': 1.": 0.8692509234307005},
{"{'LRInv2.npy': 1.0}": 0.845405935963117,
 "{'messages_equilibre_ok.npy': 0.1, 'LRInv2.npy': 0.9}": 0.8504515528761887,
 "{'messages_equilibre_ok.npy': 0.2, 'LRInv2.npy': 0.8}": 0.858085828192743,
 "{'messages_equilibre_ok.npy': 0.30000000000000004, 'LRInv2.npy': 0.7}": 0.8628163176258974,
 "{'messages_equilibre_ok.npy': 0.4, 'LRInv2.npy': 0.6}": 0.8671678646809061,
 "{'messages_equilibre_ok.npy': 0.5, 'LRInv2.npy': 0.5}": 0.8722720528174056,
 "{'messages_equilibre_ok.npy': 0.6, 'LRInv2.npy': 0.4}": 0.8730246155905395,
 "{'messages_equilibre_ok.npy': 0.7000000000000001, 'LRInv2.npy': 0.29999999999999993}": 0.8734146684686419,
 "{'messages_equilibre_ok.npy': 0.8, 'LRInv2.npy': 0.19999999999999996}": 0.8730952773585138,
 "{'messages_equilibre_ok.npy': 0.9, 'LRInv2.npy': 0.09999999999999998}": 0.8710732104684066,
 "{'messages_equilibre_ok.npy': 1.": 0.8692509234307005},
{"{'LRInv3.npy': 1.0}": 0.8461662207890495,
 "{'messages_equilibre_ok.npy': 0.1, 'LRInv3.npy': 0.9}": 0.8514056134957191,
 "{'messages_equilibre_ok.npy': 0.2, 'LRInv3.npy': 0.8}": 0.8545840920368957,
 "{'messages_equilibre_ok.npy': 0.30000000000000004, 'LRInv3.npy': 0.7}": 0.8622627725224993,
 "{'messages_equilibre_ok.npy': 0.4, 'LRInv3.npy': 0.6}": 0.8649732320490339,
 "{'messages_equilibre_ok.npy': 0.5, 'LRInv3.npy': 0.5}": 0.8698106616647951,
 "{'messages_equilibre_ok.npy': 0.6, 'LRInv3.npy': 0.4}": 0.8741532093640092,
 "{'messages_equilibre_ok.npy': 0.7000000000000001, 'LRInv3.npy': 0.29999999999999993}": 0.8723747602644284,
 "{'messages_equilibre_ok.npy': 0.8, 'LRInv3.npy': 0.19999999999999996}": 0.8729336724607011,
 "{'messages_equilibre_ok.npy': 0.9, 'LRInv3.npy': 0.09999999999999998}": 0.8706495345600853,
 "{'messages_equilibre_ok.npy': 1.": 0.8692509234307005},
{"{'LRInvTotal.npy': 1.0}": 0.8423471257324868,
 "{'messages_equilibre_ok.npy': 0.1, 'LRInvTotal.npy': 0.9}": 0.8496933912212963,
 "{'messages_equilibre_ok.npy': 0.2, 'LRInvTotal.npy': 0.8}": 0.855329115294408,
 "{'messages_equilibre_ok.npy': 0.30000000000000004, 'LRInvTotal.npy': 0.7}": 0.8579836751239401,
 "{'messages_equilibre_ok.npy': 0.4, 'LRInvTotal.npy': 0.6}": 0.8635652969746916,
 "{'messages_equilibre_ok.npy': 0.5, 'LRInvTotal.npy': 0.5}": 0.8696675341042228,
 "{'messages_equilibre_ok.npy': 0.6, 'LRInvTotal.npy': 0.4}": 0.8736032600936193,
 "{'messages_equilibre_ok.npy': 0.7000000000000001, 'LRInvTotal.npy': 0.29999999999999993}": 0.8737187601239078,
 "{'messages_equilibre_ok.npy': 0.8, 'LRInvTotal.npy': 0.19999999999999996}": 0.8729569324516924,
 "{'messages_equilibre_ok.npy': 0.9, 'LRInvTotal.npy': 0.09999999999999998}": 0.8708257527471419,
 "{'messages_equilibre_ok.npy': 1.": 0.8692509234307005}]

# Table of Dic -> Table of Table
gradLabelsTable = ["alea1", "POS1", "LRInv1", "LRInv2", "LRInv3", "LRInvTotal"]
gradValsTable = [[x for x in grad.values()][::-1] for grad in gradTable]
xaxisTicks = [0., .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.]
# Convert to pandas
df = pandas.DataFrame(gradValsTable, index=gradLabelsTable, columns=xaxisTicks).transpose()

ax = df.plot()
ax.set_xticks(xaxisTicks)
ax.set_xlabel("Poids des embbeddings réordonnancés")
ax.set_ylabel("Résultats")
ax.xaxis.grid(True)
matplotlib.pyplot.savefig("fig_grad_mix_embd.svg")

