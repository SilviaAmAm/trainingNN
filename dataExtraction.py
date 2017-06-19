import ImportData
import numpy as np

# ImportData.MolproToCSV("/Users/walfits/Repositories/trainingdata/per-user-trajectories/CH4+CN/pruning/level1_Molpro", "pbe-sto-3g-u.out")

X1, y1, Q1 = ImportData.loadPd_q("dataSets/pbe_b3lyp_partQ.csv")
X3, y3, Q3 = ImportData.loadPd_q("dataSets/pbe_b3lyp_partQ_test.csv")
X2, y2 = ImportData.loadPd("dataSets/tot-pbe-b3lyp.csv")

for i in range(len(y1)):
    if X1[i] == X3[i]:
        print "The two " + str(i) + " Xs are equal."
    else:
        print "The two " + str(i) + " Xs are different."

    if np.array_equal(y1[i], y3[i]):
        print "The two " + str(i) + " ys are equal."
    else:
        print "The two " + str(i) + " ys are different."