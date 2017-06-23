import NNFlow
import pickle

silvia = NNFlow.MLPRegFlow(max_iter=1000)
pickle.dump(silvia, open('optimisation/RSCM/attempt2/model.pickl','wb'))