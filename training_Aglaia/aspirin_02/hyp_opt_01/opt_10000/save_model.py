import sys
sys.path.append('/mnt/storage/home/sa16246/repositories/Aglaia')
import tensorflow as tf
import Neural_net_2 as nn
import pickle

estimator = nn.MLPRegFlow(max_iter=500, hidden_layer_sizes=(80,), batch_size=2000, descriptor="inverse_dist")
pickle.dump(estimator, open('/mnt/storage/home/sa16246/repositories/trainingNN/training_Aglaia/aspirin_02/hyp_opt_01/opt_10000/model.pickl','wb'))
