import NNFlow
import pickle

silvia = NNFlow.MLPRegFlow(max_iter=500, batch_size=1000)
pickle.dump(silvia, open('optimisation/PCCM/model.pickl','wb'))