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


# Starting the timer
startTime = datetime.now()

# Importing the data
X, y, Q = ImportData.loadPd_q("dataSets/PBE_B3LYP/pbe_b3lyp_partQ_rel.csv")
# X, y, Q = ImportData.loadPd_q("dataSets/pbe_b3lyp_Q_test_abs.csv")

# X = X[0:2000]
# y = y[0:2000]

# Creating the descriptors
# PCCM24 = PartialCharge.PartialCharges(X, y, Q)
# descriptor, y = PCCM24.generatePCCM24(numRep=5)
# CM = CoulombMatrix.CoulombMatrix(matrixX=X)
# descriptor, y = CM.generateRSCM(y_data=y, numRep=5)
# descriptor = CM.generateES()
# descriptor = CM.generateSCM()
# PCCM = PartialCharge.PartialCharges(X, y, Q)
# descriptor, y = PCCM.generatePCCM(numRep=5)
# DPCCM = PartialCharge.PartialCharges(X, y, Q)
# descriptor = DPCCM.generateDiagPCCM()
# descriptor = CoulombMatrix.CoulombMatrix(matrixX=X)
# X_coul = descriptor.generateTrimmedCM()
descriptor = PartialCharge.PartialCharges(X, y, Q)
X_pccm, y_pccm = descriptor.generateUnrandomisedPCCM()

# Normalising the data
# X_scal = preproc.StandardScaler().fit_transform(X_coul)
# X_scal[:,0] = 0.0
# X_scal[:,-1] = 0.0
# X_scal[:,-3] = 0.0

# Split into training and test set
X_train, X_test, y_train, y_test = modsel.train_test_split(X_pccm, y, test_size=0.2)

# Name of the model
filename = 'SavedModels/test_NN4.sav'

# Checking if a trained model of the NN exists
if os.path.isfile(filename):
    estimator = pickle.load(open(filename, 'rb'))
else:
    # Defining the estimator
    estimator = NNFlow.MLPRegFlow(max_iter=2800, batch_size=50, alpha=0.0002, learning_rate_init=0.0005, hidden_layer_sizes=(69,))

    # Set up the cross validation set, for doing 5 k-fold validation
    cv_iter = modsel.KFold(n_splits=5)

    # Training the neural net
    estimator.fit(X_train, y_train, X_test, y_test)
    estimator.plotLearningCurve()

    # Saving the model
    pickle.dump(estimator, open(filename, 'wb'))

r2, rmse, mae, lpo, lno = estimator.scoreFull(X_test, y_test)
print "On test set:"
print "R^2: " + str(r2)
print "rmse (kJ/mol): " + str(rmse)
print "mae (kJ/mol): " + str(mae)
print "The largest positive outlier (kJ/mol): " + str(lpo)
print "The largest negative outlier (kJ/mol): " + str(lno)

# Calculating the predictions
y_pred = estimator.predict(X_test)

# Correlation plot
plotting.plotSeaborn(y_test, y_pred, ylim=(-0.075,0.040), xlim=(-0.075,0.040))

# Ending the timer
endTime = datetime.now()
finalTime = endTime - startTime

print "Evaluation took " + str(finalTime)