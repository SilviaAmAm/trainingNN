import ImportData
import CoulombMatrix
import FFtraversal
import numpy as np
import NNFlow
from sklearn import model_selection as modsel

X, y, Q = ImportData.loadPd_q("dataSets/PBE_B3LYP/pbe_b3lyp_partQ_rel.csv")


X = X[:10000][:]
y = y[:10000]

# Generating coulomb matrix and trimmed coulomb matrix
CM = CoulombMatrix.CoulombMatrix(matrixX=X)
X_tcm = CM.generateTrimmedCM()

# Using the trimmed coulomb matrix to figure out the best splitting of training set and test set
# train_idx = FFtraversal.fft_idx(X_tcm, int(0.8 * X_tcm.shape[0]))
train_idx = np.load("train_idx.npy")
print len(train_idx)

# Splitting the data set
X_train = []
y_train = []

for item in train_idx:
    X_train.append(X[item])
    y_train.append(y[item])

X_test = np.delete(X, train_idx, axis=0)
y_test = np.delete(y, train_idx, axis=0)

# Generating the descriptor for the train set
des_train = CoulombMatrix.CoulombMatrix(matrixX=X_train)
X_prcm_train, y_train = des_train.generatePRCM(y_train,numRep=8)

# Generating the descriptor for the test set
des_test = CoulombMatrix.CoulombMatrix(matrixX=X_test)
X_prcm_test, y_test = des_test.generatePRCM(y_test,numRep=8)

# Defining the estimator
estimator = NNFlow.MLPRegFlow(max_iter=2800, batch_size=500, alpha=0.0005, learning_rate_init=0.0002, hidden_layer_sizes=(51,))

# Set up the cross validation set, for doing 5 k-fold validation
cv_iter = modsel.KFold(n_splits=5)

# Training the neural net
estimator.fit(X_prcm_train, y_train, X_prcm_test, y_test)
estimator.plotLearningCurve()
estimator.errorDistribution(X_prcm_test, y_test)

r2, rmse, mae, lpo, lno = estimator.scoreFull(X_prcm_test, y_test)
print "On test set:"
print "R^2: " + str(r2)
print "rmse (kJ/mol): " + str(rmse)
print "mae (kJ/mol): " + str(mae)
print "The largest positive outlier (kJ/mol): " + str(lpo)
print "The largest negative outlier (kJ/mol): " + str(lno)


# Correlation plot
estimator.correlationPlot(X_prcm_test, y_test, ylim=(-0.075,0.040), xlim=(-0.075,0.040))
