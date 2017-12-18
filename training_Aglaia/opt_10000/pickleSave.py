import sys
sys.path.append('/Users/walfits/Repositories/Aglaia')
import tensorflow as tf
import Neural_net_2 as nn
import pickle

estimator = nn.MLPRegFlow(max_iter=500, hidden_layer_sizes=(80,), batch_size=2000, descriptor="inverse_dist")
pickle.dump(estimator, open('/Users/walfits/Repositories/trainingNN/training_Aglaia/opt_10000/model.pickl','wb'))
