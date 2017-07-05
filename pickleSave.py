import NNFlow
import pickle

silvia = NNFlow.MLPRegFlow(max_iter=1000)
pickle.dump(silvia, open('/Users/walfits/Repositories/trainingNN/optimisation/PBE_B3LYP/test/PCCM/notscal/model.pickl','wb'))