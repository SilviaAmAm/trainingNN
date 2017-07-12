import sys
sys.path.append('/mnt/storage/home/sa16246/repositories/YAMLP/SciFlow')
import NNFlow
import pickle

silvia = NNFlow.MLPRegFlow(max_iter=1000)
pickle.dump(silvia, open('/mnt/storage/home/sa16246/repositories/trainingNN/optimisation/PBE_B3LYP/PRCM/not_scal/model.pickl','wb'))
