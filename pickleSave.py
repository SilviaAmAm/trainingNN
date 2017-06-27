import NNFlow
import pickle

silvia = NNFlow.MLPRegFlow(max_iter=1000)
pickle.dump(silvia, open('optimisation/DPCCM/attempt1/model.pickl','wb'))