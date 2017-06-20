import NNFlow
import pickle

silvia = NNFlow.MLPRegFlow(max_iter=1500)
pickle.dump(silvia, open('optimisation/RSCM/model.pickl','wb'))