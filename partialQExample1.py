"""
This script uses the total PBE/B3LYP dataset (relative energies) with partial charges to fit a neural network.
It uses Gridsearch.
"""

import ImportData
import PartialCharge
import CoulombMatrix
import NNFlow
import plotting
from sklearn import preprocessing as preproc
from sklearn import model_selection as modsel
from datetime import datetime

# Starting the timer
startTime = datetime.now()

# Importing the data
X, y, Q = ImportData.loadPd_q("dataSets/pbe_b3lyp_partQ_rel.csv")
# X, y, Q = ImportData.loadPd_q("dataSets/pbe_b3lyp_Q_test_abs.csv")

X = X[0:1500]
y = y[0:1500]

# Creating the descriptors
# PCCM = PartialCharge.PartialCharges(X, y, Q)
# PCCM.generatePCCM(numRep=3)
# descriptor, y = PCCM.getPCCM()
CM = CoulombMatrix.CoulombMatrix(matrixX=X)
descriptor, y = CM.generateRSCM(y_data=y, numRep=5)
# descriptor = CM.generateES()
# descriptor = CM.generateSCM()

# Normalising the data
X_scal = preproc.StandardScaler().fit_transform(descriptor)

# Split into training and test set
X_train, X_test, y_train, y_test = modsel.train_test_split(X_scal, y, test_size=0.2)

# Defining the estimator
estimator = NNFlow.MLPRegFlow(max_iter=1500, batch_size=50, alpha=0, learning_rate_init=0.0002, hidden_layer_sizes=(45,))

# Set up the cross validation set, for doing 5 k-fold validation
cv_iter = modsel.KFold(n_splits=5)

# Dictionary of hyper parameters to optimise
# hypPar = {}
# hypPar.update({"learning_rate_init":[0.00005, 0.0001, 0.0005, 0.001]})
# hypPar.update({"hidden_layer_sizes":[(40,), (46,), (48,), (50,)]})
# hypPar.update({"alpha":[0.255, 0.26, 0.265, 0.270]})

# grid_search = modsel.GridSearchCV(estimator=estimator,param_grid=hypPar,cv=cv_iter, n_jobs=4)
#
# # Fitting the model
# grid_search.fit(X_train,y_train)
estimator.fit(X_train, y_train, X_test, y_test)
# estimator.plotTrainCost()
estimator.plotLearningCurve()

# Printing the best parameters
# print "The best parameters are " + str(grid_search.best_params_)
# print "The best R2 value obtained (on cross val set) is " + str(grid_search.best_score_)
#
# # Setting the best parameters in the estimator
# estimator.set_params(alpha=grid_search.best_params_["alpha"], learning_rate_init=grid_search.best_params_["learning_rate_init"], hidden_layer_sizes=grid_search.best_params_["hidden_layer_sizes"] )
# estimator.fit(X_train,y_train)
# estimator.plotTrainCost()


r2, rmse, mae = estimator.scoreFull(X_test, y_test)
print "On test set:"
print "R^2: " + str(r2)
print "rmse (kJ/mol): " + str(rmse)
print "mae (kJ/mol): " + str(mae)

# Calculating the predictions
y_pred = estimator.predict(X_test)

# Correlation plot
plotting.plotSeaborn(y_test, y_pred)

# Ending the timer
endTime = datetime.now()
finalTime = endTime - startTime

print "Evaluation took " + str(finalTime)