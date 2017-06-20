"""
This tests the random coulomb matrix and checks that the random repetitions still have the same eigen spectrum.
"""

import CoulombMatrix
import ImportData
import numpy.testing as npt
import numpy.linalg as LA
import numpy as np


X, y, Q = ImportData.loadPd_q("dataSets/pbe_b3lyp_Q_test_abs.csv")
CM = CoulombMatrix.CoulombMatrix(matrixX=X)
# CM.generateES()
# CM.generateSCM()
X, y = CM.generateRSCM(y, numRep=5)

# CM.plot(X, 5)
# CM.plot(X, 4)
# CM.plot(X, 3)
# CM.plot(X, 2)


for i in range(11, 15):
    print i
    npt.assert_almost_equal(np.sort(LA.eigvals(np.reshape(X[10], (7, 7)))),np.sort(LA.eigvals(np.reshape(X[i], (7, 7)))), decimal=7)
