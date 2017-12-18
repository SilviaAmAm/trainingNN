"""
This script uses partial charges as the descriptor to fit a neural network.
The hyperparameters are input manually after they have been optimised with Osprey.
It enables to save the model to a file.
"""

import ImportData
import PartialCharge
import CoulombMatrix
import NNFlow
import CoulombMatrix
import plotting
from sklearn import preprocessing as preproc
from sklearn import model_selection as modsel
from datetime import datetime
import pickle
import os.path
import numpy as np


# Starting the timer
startTime = datetime.now()
saveModel = True

# Importing the data
X, y, Q = ImportData.loadPd_q("dataSets/PBE_B3LYP/pbe_b3lyp_partQ_rel.csv")

# Creating the descriptors
# PCCM24 = PartialCharge.PartialCharges(X, y, Q)
# descriptor, y = PCCM24.generatePCCM24(numRep=5)
# CM = CoulombMatrix.CoulombMatrix(matrixX=X)
# descriptor, y = CM.generateRSCM(y_data=y, numRep=5)
# descriptor = CM.generateES()
# descriptor = CM.generateSCM()
# descriptor, y = CM.generatePRCM(y, numRep=5)
PCCM = PartialCharge.PartialCharges(X, y, Q)
descriptor, y = PCCM.generatePCCM(numRep=5)
# descriptor, y = PCCM.hybrid_pccm_2(numRep=5)
# DPCCM = PartialCharge.PartialCharges(X, y, Q)
# descriptor = DPCCM.generateDiagPCCM()
# descriptor = CoulombMatrix.CoulombMatrix(matrixX=X)
# X_coul = descriptor.generateTrimmedCM()
# descriptor = PartialCharge.PartialCharges(X, y, Q)
# X_pccm, y_pccm = descriptor.generateUnrandomisedPCCM()

# Hybrid 3 - pccm + nuclear charges at the end
nc = np.zeros(7)
nc[0:4] = 1.0
nc[4:6] = 6.0
nc[6] = 7.0
nc_big = np.tile(nc, (descriptor.shape[0],1))
descriptor = np.concatenate((descriptor, nc_big), axis = 1)

# Normalising the data
# X_scal = preproc.StandardScaler().fit_transform(descriptor)
X_scal = descriptor

# Split into training and test set
X_train, X_test, y_train, y_test = modsel.train_test_split(X_scal, y, test_size=0.2)
# Name of the model
filename = 'SavedModels/hyb3.sav'

# Checking if a trained model of the NN exists
if os.path.isfile(filename):
    estimator = pickle.load(open(filename, 'rb'))
else:
    # Defining the estimator
    estimator = NNFlow.MLPRegFlow(max_iter=2800, batch_size=355, alpha=0.00001, learning_rate_init=0.0003, hidden_layer_sizes=(29,))

    # Training the neural net
    estimator.fit(X_train, y_train, X_test, y_test)
    estimator.plotLearningCurve()
    estimator.errorDistribution(X_test, y_test)

    # Saving the model
    if saveModel:
        pickle.dump(estimator, open(filename, 'wb'))

r2, rmse, mae, lpo, lno = estimator.scoreFull(X_test, y_test)
print "On test set:"
print "R^2: " + str(r2)
print "rmse (kJ/mol): " + str(rmse * 2625.50)
print "mae (kJ/mol): " + str(mae * 2625.50)
print "The largest positive outlier (kJ/mol): " + str(lpo * 2625.50)
print "The largest negative outlier (kJ/mol): " + str(lno * 2625.50)

# Calculating the predictions
y_pred = estimator.predict(X_test)

# Correlation plot
estimator.correlationPlot(X_test, y_test, ylim=(-0.075,0.040), xlim=(-0.075,0.040))

# Plotting the weights1
estimator.plotWeights()

# estimator.vis_input_matrix(X_train[0,:])
# estimator.vis_input_network(X_train[0,:])

# Ending the timer
endTime = datetime.now()
finalTime = endTime - startTime

print "Evaluation took " + str(finalTime)