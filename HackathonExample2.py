"""
This script uses the new estimator written in tensorflow, with added gridsearch, to fit the data that was
used in the hackathon (PBE/B3LYP data set with absolute energies). The hyperparameters are optimised through the gridsearch. The data set contains absolute energies.
"""

import CoulombMatrix
import ImportData
import NNFlow
import plotting
import numpy as np
from sklearn import preprocessing as preproc
from sklearn import model_selection as modsel
from datetime import datetime

# Starting the timer
startTime = datetime.now()

# Importing the data
X, y = ImportData.loadPd("dataSets/tot-pbe-b3lyp.csv")

# Creating the CM object
coulMat = CoulombMatrix.CoulombMatrix(matrixX=X)
#  Creating the three descriptors
# descript = coulMat.generateES()
# descript = coulMat.generateSCM()
descript, y = coulMat.generateRSCM(y_data=y, numRep=1)

# Normalising the data
X_scal = preproc.StandardScaler().fit_transform(descript)

# Split into training and test set
X_train, X_test, y_train, y_test = modsel.train_test_split(X_scal, y, test_size=0.1)

# Defining the estimator
estimator = NNFlow.MLPRegFlow(max_iter=500, batch_size=1000)

# Set up the cross validation set, for doing 5 k-fold validation
cv_iter = modsel.KFold(n_splits=5)

# Dictionary of hyper parameters to optimise
hypPar = {}
hypPar.update({"learning_rate_init":[0.00005, 0.0001, 0.0005, 0.001]})
hypPar.update({"hidden_layer_sizes":[(40,), (46,), (48,), (50,)]})
hypPar.update({"alpha":[0.255, 0.26, 0.265, 0.270]})

grid_search = modsel.GridSearchCV(estimator=estimator,param_grid=hypPar,cv=cv_iter, n_jobs=4)

# Fitting the model
grid_search.fit(X_train,y_train)

# Printing the best parameters
print "The best parameters are " + str(grid_search.best_params_)
print "The best R2 value (on cross val set) obtained is " + str(grid_search.best_score_)

# # Setting the best parameters in the estimator
# estimator.set_params(alpha=grid_search.best_params_["alpha"])
estimator.fit(X_train,y_train)
estimator.plotTrainCost()

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